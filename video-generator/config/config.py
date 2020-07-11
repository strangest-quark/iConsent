class Config(object):
    RESULT_S3_BUCKET = 'iconsent-videos'
    image_map = dict()
    lang_map = dict()
    input_map = dict()
    VIDEO_SIZE = (640, 240)
    BLUE = (59 / 255, 89 / 255, 152 / 255)
    GREEN = (176 / 255, 210 / 255, 63 / 255)
    WHITE = (255, 255, 255)
    WHITE_GIZEH = (1, 1, 1)
    DURATION = 5


class DevelopmentConfig(Config):
    LOCAL = True
    SB_LOGO_PATH_PREFIX = '/Users/sn5/git/other/iConsent/video/assets/logo/'
    SB_AUDIO_PATH_PREFIX = '/Users/sn5/git/other/iConsent/video/assets/'
    SB_VIDEO_PATH_PREFIX = '/Users/sn5/git/other/iConsent/video/assets/'
    LANG_PATH = '/Users/sn5/git/other/iConsent/video/config/languages/'
    CONFIG_PATH = '/Users/sn5/git/other/iConsent/video/config/'


class ProductionConfig(Config):
    LOCAL = False
    SB_LOGO_PATH_PREFIX = '/var/task/assets/logo/'
    SB_AUDIO_PATH_PREFIX = '/tmp/'
    SB_VIDEO_PATH_PREFIX = '/tmp/'
    LANG_PATH = '/var/task/config/languages/'
    CONFIG_PATH = '/var/task/config/'
