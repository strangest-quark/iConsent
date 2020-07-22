import json
import random
from config.config import ProductionConfig
import boto3
import botocore
import requests

lambda_client = boto3.client('lambda', region_name='ap-south-1')
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('iconsent')

fiu_list = ['Quickbooks', 'Mint', 'Monito', 'Zoho', 'Freshworks', 'ClearTax', 'FastBooks', 'EasyTax', 'Paisato']
non_verified = ['FastBooks', 'EasyTax', 'Paisato']
fip_list = ['Axis Bank', 'Citibank', 'HDFC Bank', 'ICICI Bank', 'SBI']

config = ProductionConfig
lang_map = dict()
image_map = dict()
s3 = boto3.resource('s3')


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
    fius = random.sample(fiu_list,
                         len(pending) + len(pending) + len(active) + len(inactive) + len(paused) + len(rejected) + len(
                             revoked))
    fips = random.sample(fip_list, len(accounts))

    pending_arr = []
    paused_arr = []
    inactive_arr = []
    revoked_arr = []
    rejected_arr = []
    active_arr = []
    fip_arr = []

    i = 0
    for account in accounts:
        fip_arr.append(account_proc(account, fips[i]))
        i = i + 1

    i = 0
    for p in pending:
        pending_arr.append(consent_proc(p, fius[i], lan, dashboard['session'], fips))
        i = i + 1

    for p in paused:
        paused_arr.append(consent_proc(p, fius[i], lan, dashboard['session'], fips))
        i = i + 1

    for p in inactive:
        inactive_arr.append(consent_proc(p, fius[i], lan, dashboard['session'], fips))
        i = i + 1

    for p in active:
        active_arr.append(consent_proc(p, fius[i], lan, dashboard['session'], fips))
        i = i + 1

    for p in paused:
        paused_arr.append(consent_proc(p, fius[i], lan, dashboard['session'], fips))
        i = i + 1

    for p in rejected:
        rejected_arr.append(consent_proc(p, fius[i], lan, dashboard['session'], fips))
        i = i + 1

    for p in revoked:
        revoked_arr.append(consent_proc(p, fius[i], lan, dashboard['session'], fips))
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
        config.VIDEO_BUCKET, video_req['req']['consentArtefactID'] + '-' + lan + '.mp4')


def check_if_key_exists(consentArtefactId):
    response = table.get_item(
        Key={
            'consentId': consentArtefactId
        }
    )
    if 'Item' in response.keys():
        res = response['Item']
        res.pop('video_req')
        return True, res
    else:
        return False, None


def put_key(consent_map):
    table.put_item(
        Item=consent_map
    )


def fill_text(text, input_map):
    while '{' in text:
        start = text.find('{')
        end = text.find('}')
        key = text[start + 1:end]
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
        elif lang_map.get('lan') == 'en-IN':
            fill = k
        else:
            fill = ""
        text = text[:start] + fill + text[end + 1:]
    return text.capitalize()


def consent_proc(consent, random_fiu, lan, session, fips):
    keyExists, res = check_if_key_exists(consent['consentArtefactID'] + '-' + lan)
    if keyExists:
        return res
    consent_map = dict()
    consent_artefact = json.loads(consent_artefact_get(consent, session))
    video_req = dict()
    video_req['fiu'] = random_fiu
    video_req['fip'] = fips
    video_req['datatype'] = [x.lower() for x in consent_artefact['info']['ConsentDetail']['consentTypes']]
    video_req['account'] = [x.lower() for x in consent_artefact['info']['ConsentDetail']['fiTypes']]
    video_req['mode'] = consent_artefact['info']['ConsentDetail']['consentMode'].lower()
    video_req['type'] = consent_artefact['info']['ConsentDetail']['fetchType'].lower()
    video_req['language'] = lan
    video_req['dataLife'] = (str(consent_artefact['info']['ConsentDetail']['DataLife']['value']) + ' ' +
                             consent_artefact['info']['ConsentDetail']['DataLife']['unit']).lower()
    video_req['consentFrom'] = consent_artefact['info']['ConsentDetail']['consentStart']
    video_req['consentTo'] = consent_artefact['info']['ConsentDetail']['consentExpiry']
    video_req['fiFrom'] = consent_artefact['info']['ConsentDetail']['FIDataRange']['from']
    video_req['fiTo'] = consent_artefact['info']['ConsentDetail']['FIDataRange']['to']
    video_req['frequency'] = (str(consent_artefact['info']['ConsentDetail']['Frequency']['value']) + ' ' +
                              consent_artefact['info']['ConsentDetail']['Frequency']['unit']).lower()
    video_req['consentArtefactID'] = consent['consentArtefactID']
    req = {"req": video_req}

    consent_map['consentArtefactID'] = consent['consentArtefactID']
    consent_map['consentId'] = consent['consentArtefactID'] + '-' + lan
    consent_map['fiu'] = lang_map[random_fiu]
    consent_map['validTill'] = lang_map['validTill'] + ' ' + date_proc(consent['expireTime'])
    consent_map['isVerified'] = True
    consent_map['tagline'] = fill_text(lang_map['tagline'], {"fiu": random_fiu, "type": video_req['account']})
    if random_fiu in non_verified:
        consent_map['isVerified'] = False
    consent_map['fiu_logo'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (config.LOGO_BUCKET, image_map[random_fiu])
    consent_map['video'] = video_invoke(req, lan)
    consent_map['video_req'] = json.dumps(req)
    put_key(consent_map)
    consent_map.pop('video_req')
    return consent_map


def account_proc(account, random_fip):
    fip_map = dict()
    fip_map['fip_logo'] = "https://s3-ap-south-1.amazonaws.com/%s/%s" % (config.LOGO_BUCKET, image_map[random_fip])
    fip_map['fip_name'] = lang_map[random_fip]
    fip_map['fip_accType'] = lang_map[account['nickName']]
    fip_map['endingNumber'] = account['maskedAccountNumber'][-4:]
    return fip_map