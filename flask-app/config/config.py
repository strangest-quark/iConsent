class Config(object):
    VIDEO_BUCKET = 'iconsent-videos'
    LOGO_BUCKET = 'iconsent-logos'


class DevelopmentConfig(Config):
    LOCAL = True
    LANG_PATH = '/Users/sn5/git/other/iConsent/assets/flask-app/config/languages/'
    CONFIG_PATH = '/Users/sn5/git/other/iConsent/assets/flask-app/config/'

class ProductionConfig(Config):
    LOCAL = False
    LANG_PATH = '/var/task/config/languages/'
    CONFIG_PATH = '/var/task/config/'
