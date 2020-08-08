import time
import json
from config.config import DevelopmentConfig
from process import process, consent_res

config = DevelopmentConfig

if __name__ == '__main__':
    with open(config.CONFIG_PATH + 'local_input.json', "r") as read_file:
        dashboard_obj = json.load(read_file)
    print(process(dashboard_obj))
    session = dashboard_obj['session']
    consentArtefactId = dashboard_obj['consentArtefactId']
    language = dashboard_obj['language']
    #print((consent_res(consentArtefactId, session, language)))