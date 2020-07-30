import json
import random

from boto3.dynamodb.conditions import Key
from config.config import ProductionConfig
import boto3
import requests
from googletrans import Translator

lambda_client = boto3.client('lambda', region_name='ap-south-1')
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table = dynamodb.Table('iconsent')

fiu_map = {
    'insurance_policies': ['ClearTax'],
    'deposit': ['Quickbooks', 'Zoho', 'Freshworks'],
    'term-deposit': ['Monito'],
    'sip': ['Mint'],
    'mutual_funds': ['Mint'],
    'nps': ['ClearTax'],
    'other': ['Mint', 'Quickbooks']
}

fip_map = {
    'insurance_policies': [['LIC', 'XX2323'], ['Max Life', 'XX4587']],
    'deposit': [['Citibank', 'XX1234'], ['SBI', 'XX4321']],
    'term-deposit': [['Axis', 'XX5432'], ['SBI', 'XX2345'], ['ICICI', 'XX4345']],
    'sip': [['HDFC', 'XX3421']],
    'nps': [['SBI', 'XX3213']],
    'mutual_funds': [['HDFC', 'XX3421']],
    'other': [['ICICI', 'XX3213']]
}

unverified_fiu_map = {
    'insurance_policies': ['EasyTax'],
    'deposit': ['Fastbooks'],
    'term-deposit': ['Paisato'],
    'sip': ['Paisato'],
    'mutual_funds': ['Paisato'],
    'nps': ['EasyTax'],
    'other': ['EasyTax', 'Fastbooks']
}

non_verified = ['EasyTax', 'Fastbooks', 'Paisato']

config = ProductionConfig
lang_map = dict()
image_map = dict()
s3 = boto3.resource('s3')
translator = Translator()

fip_list = ['Citibank', 'LIC', 'Axis Bank', 'HDFC Bank', ]


def process(dashboard):
    global lang_map
    global image_map
    lan = dashboard['language']
    with open(config.LANG_PATH + lan + ".json", "r") as read_file:
        lang_map = json.load(read_file)
    with open(config.CONFIG_PATH + 'images.json', "r") as read_file:
        image_map = json.load(read_file)

    accounts = dashboard['bankAccounts']
    pending = dashboard['consents']['pending']
    active = dashboard['consents']['active']
    inactive = dashboard['consents']['inactive']
    paused = dashboard['consents']['paused']
    rejected = dashboard['consents']['rejected']
    revoked = dashboard['consents']['revoked']
    fips = random.sample(fip_list, len(accounts))

    pending_arr = []
    paused_arr = []
    inactive_arr = []
    revoked_arr = []
    rejected_arr = []
    active_arr = []
    fip_arr = []

    i = 0
    fip_arr = account_proc()

    i = 0
    for p in pending:
        pending_arr.append(consent_proc(p, lan, dashboard['session'], True))
        if i == len(pending) - 1:
            pending_arr.append(consent_proc(p, lan, dashboard['session'], True, True))
        i = i + 1

    for p in paused:
        paused_arr.append(consent_proc(p, lan, dashboard['session']))
        i = i + 1

    for p in inactive:
        inactive_arr.append(consent_proc(p, lan, dashboard['session']))
        i = i + 1

    for p in active:
        active_arr.append(consent_proc(p, lan, dashboard['session']))
        i = i + 1

    for p in paused:
        paused_arr.append(consent_proc(p, lan, dashboard['session']))
        i = i + 1

    for p in rejected:
        rejected_arr.append(consent_proc(p, lan, dashboard['session']))
        i = i + 1

    for p in revoked:
        revoked_arr.append(consent_proc(p, lan, dashboard['session']))
        i = i + 1

    res_map = dict()
    res_map['active'] = active_arr
    res_map['inactive'] = inactive_arr
    res_map['paused'] = paused_arr
    res_map['pending'] = pending_arr
    res_map['rejected'] = rejected_arr
    res_map['revoked'] = revoked_arr
    res_map['accounts'] = fip_arr
    return res_map


def date_proc(ts):
    d_arr = ts.split('-')
    m_day = d_arr[2][0:2]
    month = lang_map[d_arr[1]]
    year = d_arr[0]
    return m_day + ' ' + month + ' ' + year


def date_ts_proc(ts):
    d_arr = ts.split('-')
    m_day = d_arr[2][0:2]
    month = d_arr[1]
    year = d_arr[0]
    return year + '-' + month + '-' + m_day


def consent_artefact_get(consent, session):
    url = 'https://api-sandbox.onemoney.in/app/consent/' + consent['consentArtefactID']
    headers = {'sessionId': session, 'Content-Type': 'application/json'}
    req = requests.get(url, headers=headers)
    return req.content


def video_invoke(video_req, lan):
    res = lambda_client.invoke(FunctionName="video-generator-dev-app",
                               InvocationType='Event',
                               Payload=json.dumps(video_req)
                               )
    return "https://s3-ap-south-1.amazonaws.com/%s/%s" % (
        config.VIDEO_BUCKET, video_req['req']['consentartefactid'] + '-' + lan + '.mp4')


def check_if_key_exists(consentArtefactIdLan):
    response = table.get_item(
        Key={
            'consentId': consentArtefactIdLan
        }
    )
    if 'Item' in response.keys():
        res = response['Item']
        res.pop('video_req')
        return True, res
    else:
        return False, None


def check_if_lang_exists(consentArtefactId):
    response = table.query(
        IndexName="consentArtefactID-index",
        KeyConditionExpression=Key('consentArtefactID').eq(consentArtefactId)
    )
    if 'Items' in response.keys() and len(response['Items']) > 0:
        return True, json.loads(response['Items'][0]['video_req'])['req']['fiu']
    else:
        return False, None


def put_key(consent_map):
    table.put_item(
        Item=consent_map
    )


def fill_text(text, input_map, iter):
    if iter == 0 and lang_map.get('lan') != 'en-IN':
        return translator.translate(text, dest=lang_map.get('lan')).text
    while '{' in text:
        start = text.find('{')
        end = text.find('}')
        key = text[start + 1:end].lower()
        if key in ['fip', 'fiu']:
            if iter == 1:
                text = list(text)
                text[start] = '('
                text[end] = ')'
                text = ''.join(text)
                continue
        if isinstance(input_map.get(key), list):
            fill = ''
            i = 0
            for ele in input_map.get(key):
                if len(input_map.get(key)) > 1 and i == len(input_map.get(key)) - 1:
                    fill = fill[:-1] + ' ' + lang_map.get('and') + ' ' + lang_map.get(ele)
                else:
                    fill = fill + lang_map.get(ele) + ','
                i = i + 1
            if fill[-1] == ',':
                fill = fill[:-1]
            text = text[:start] + fill + text[end + 1:]
            continue
        else:
            k = input_map.get(key)
        if k in lang_map:
            fill = lang_map.get(k)
        else:
            fill = k
        text = text[:start] + fill + text[end + 1:]
    if (iter == 1 or iter == 0) and lang_map.get('lan') == 'en-IN':
        return text.replace('(', '{').replace(')', '}')
    if iter == 1:
        return translator.translate(text, dest=lang_map.get('lan')).text.replace('(', '{').replace(')', '}')
    else:
        return text.capitalize()


def get_fip(account):
    lists = fip_map[account]
    res = []
    for element in lists:
        res.append(element[0])
    return res


def consent_proc(consent, lan, session, isVideo=False, isLast=False):
    keyExists, res = check_if_key_exists(consent['consentArtefactID'] + '-' + lan)
    if keyExists:
        return res
    else:
        consent_artefact = json.loads(consent_artefact_get(consent, session))
        video_req = dict()
        video_req['datatype'] = [x.lower() for x in consent_artefact['info']['ConsentDetail']['consentTypes']]
        video_req['account'] = [x.lower() for x in consent_artefact['info']['ConsentDetail']['fiTypes']]
        video_req['fip'] = get_fip(video_req['account'][0])
        keyExists, res = check_if_lang_exists(consent['consentArtefactID'])
        if keyExists:
            random_fiu = res
        else:
            if not isLast:
                fius_map = fiu_map
            else:
                fius_map = unverified_fiu_map
            if video_req['account'][0] in fius_map:
                random_fiu = random.sample(fius_map[video_req['account'][0]], 1)[0]
            else:
                random_fiu = random.sample(fius_map['other'], 1)[0]
    consent_map = dict()
    video_req['fiu'] = random_fiu
    video_req['mode'] = consent_artefact['info']['ConsentDetail']['consentMode'].lower()
    video_req['type'] = consent_artefact['info']['ConsentDetail']['fetchType'].lower()
    video_req['language'] = lan
    video_req['datalife'] = (str(consent_artefact['info']['ConsentDetail']['DataLife']['value']) + ' ' +
                             consent_artefact['info']['ConsentDetail']['DataLife']['unit']).lower()
    video_req['consentfrom'] = date_ts_proc(consent_artefact['info']['ConsentDetail']['consentStart'])
    video_req['consentto'] = date_ts_proc(consent_artefact['info']['ConsentDetail']['consentExpiry'])
    video_req['fifrom'] = date_ts_proc(consent_artefact['info']['ConsentDetail']['FIDataRange']['from'])
    video_req['fito'] = date_ts_proc(consent_artefact['info']['ConsentDetail']['FIDataRange']['to'])
    video_req['frequency'] = (str(consent_artefact['info']['ConsentDetail']['Frequency']['value']) + ' ' +
                              consent_artefact['info']['ConsentDetail']['Frequency']['unit']).lower()
    video_req['consentartefactid'] = consent['consentArtefactID']
    req = {"req": video_req}

    consent_map['consentArtefactID'] = consent['consentArtefactID']
    consent_map['consentId'] = consent['consentArtefactID'] + '-' + lan
    consent_map['fiu'] = lang_map[random_fiu]
    consent_map['validTill'] = lang_map['validTill'] + ' ' + date_proc(consent['expireTime'])
    consent_map['isVerified'] = True
    consent_map['tagline'] = fill_text(
        fill_text(lang_map['tagline'], {"fiu": random_fiu, "type": video_req['account']}, 1),
        {"fiu": random_fiu, "type": video_req['account']}, 2)
    if video_req['fiu'] in non_verified:
        consent_map['isVerified'] = False
    consent_map['fiu_logo'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (config.LOGO_BUCKET, image_map[random_fiu])
    if (isVideo):
        consent_map['video'] = video_invoke(req, lan)
    else:
        consent_map['video'] = "no link"
    consent_map['video_req'] = json.dumps(req)
    put_key(consent_map)
    print(consent_map)
    consent_map.pop('video_req')
    return consent_map


def account_proc():
    fip_list = []
    for key in fip_map:
        iter_list = fip_map[key]
        for element in iter_list:
            fip = dict()
            fip['fip_logo'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (
                config.LOGO_BUCKET, image_map[element[0]])
            fip['fip_name'] = lang_map[element[0]]
            fip['fip_accType'] = lang_map[key]
            fip['endingNumber'] = element[1]
            fip_list.append(fip)
    return fip_list


def consent_account_proc(accType):
    fip_list = []
    iter_list = fip_map[accType]
    for element in iter_list:
        fip = dict()
        fip['fip_logo'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (
            config.LOGO_BUCKET, image_map[element[0]])
        fip['fip_name'] = lang_map[element[0]]
        fip['fip_accType'] = lang_map[accType]
        fip['endingNumber'] = element[1]
        fip_list.append(fip)
    return fip_list


def consent_res(consentArtefactId, session, lan):
    keyExists, res = check_if_lang_exists(consentArtefactId)
    if keyExists:
        fiu = res
    global lang_map
    global image_map
    with open(config.LANG_PATH + lan + ".json", "r") as read_file:
        lang_map = json.load(read_file)
    with open(config.CONFIG_PATH + 'images.json', "r") as read_file:
        image_map = json.load(read_file)
    consent_artefact = json.loads(consent_artefact_get({"consentArtefactID": consentArtefactId}, session))
    input_map = {
        "fiu": fiu,
        "type": [x.lower() for x in consent_artefact['info']['ConsentDetail']['fiTypes']],
        "from": date_proc(consent_artefact['info']['ConsentDetail']['FIDataRange']['from']),
        "to": date_proc(consent_artefact['info']['ConsentDetail']['FIDataRange']['to']),
        "valid": date_proc(consent_artefact['info']['ConsentDetail']['consentExpiry']),
        "purpose": consent_artefact['info']['ConsentDetail']['Purpose']['text'],
        "datatype": [x.lower() for x in consent_artefact['info']['ConsentDetail']['consentTypes']],
        "mode": consent_artefact['info']['ConsentDetail']['consentMode'].lower(),
        "frequency": (str(consent_artefact['info']['ConsentDetail']['Frequency']['value']) + ' ' +
                      consent_artefact['info']['ConsentDetail']['Frequency']['unit']).lower(),
        "datalife": (str(consent_artefact['info']['ConsentDetail']['DataLife']['value']) + ' ' +
                     consent_artefact['info']['ConsentDetail']['DataLife']['unit']).lower(),
        "fetchtype": consent_artefact['info']['ConsentDetail']['fetchType'].lower()
    }
    print(input_map['datalife'])
    print(input_map['mode'])
    consent = dict()
    consent['tagline'] = fill_text(fill_text(lang_map['tagline'], input_map, 1), input_map, 2)
    consent['q1'] = fill_text(fill_text(lang_map['q1'], input_map, 1), input_map, 2)
    consent['q2'] = lang_map['q2']
    consent['q3'] = lang_map['q3']
    consent['q4'] = fill_text(fill_text(lang_map['q4'], input_map, 1).capitalize(), input_map, 2)
    consent['ans1'] = fill_text(fill_text(lang_map['ans1'], input_map, 1), input_map, 2)
    consent['from'] = lang_map['from']
    consent['to'] = lang_map['to']
    consent['fromDate'] = input_map['from']
    consent['toDate'] = input_map['to']
    consent['validTill'] = lang_map['validTill'] + ' ' + input_map['valid']
    input_map['datalife'] = frequency_proc(input_map['datalife'])
    input_map['frequency'] = frequency_proc(input_map['frequency'])
    consent['card1_icon'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (
        config.LOGO_BUCKET, image_map[input_map['fetchtype']])
    consent['card2_icon'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (
        config.LOGO_BUCKET, image_map[input_map['mode']])
    consent['card3_icon'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (
        config.LOGO_BUCKET, image_map[','.join(input_map['datatype'])])
    consent['accounts'] = consent_account_proc(input_map["type"][0])
    consent['fiu_logo'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (config.LOGO_BUCKET, image_map[fiu])
    consent['video'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (config.VIDEO_BUCKET, consentArtefactId + '-' + lan + '.mp4')
    consent['isVerified'] = fiu not in non_verified
    consent["ans4"] = fill_text(fill_text(lang_map['ans4'], input_map, 1),input_map, 2).capitalize()
    consent["bank_ques"] = lang_map['bank_ques']
    consent["hurray_1"] = lang_map['hurray_1']
    consent["hurray_2"] = lang_map['hurray_2']
    consent["hurray_3"] = lang_map['hurray_3']
    consent["warn_1"] = lang_map['warn_1']
    consent["warn_2"] = lang_map['warn_2']
    consent["warn_3"] = lang_map['warn_3']
    consent['hurray_4'] = fill_text(fill_text(lang_map['hurray_4'], input_map, 1), input_map, 2).capitalize()
    if input_map['mode'] == 'store':
        consent["ans4"] = consent["ans4"] + ' ' + fill_text(fill_text(lang_map['ans4_suffix'], input_map, 1),input_map, 2).capitalize()
    return consent


def frequency_proc(freq):
    freq = freq.split(' ')
    freq[1] = lang_map[freq[1]]
    return ' '.join(freq)
