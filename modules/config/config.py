class Config(object):
    RESULT_S3_BUCKET = 'iconsent-videos'
    image_map = dict()
    lang_map = dict()
    input_map = dict()
    VIDEO_SIZE = (640, 360)
    BLUE = (59 / 255, 89 / 255, 152 / 255)
    GREEN = (176 / 255, 210 / 255, 63 / 255)
    WHITE = (255, 255, 255)
    WHITE_GIZEH = (1, 1, 1)
    DURATION = 5
    ICON_HEIGHT = 150
    ICON_WIDTH = 100
    ICON_SIZE = 100
    GRID_ICON_SIZE = 120
    DEFAULT_FRAME_DURATION = 5
    static_keys = ['fip', 'fiu']
    span = [[(-50, 0)], [(-170, 0), (80, 0)], [(-150, 0), (-30, 0), (100, 0)]]
    grid = {
        "center": 2,
        "left": 6,
        "right": 1
    }


class DevelopmentConfig(Config):
    LOCAL = True
    SB_LOGO_PATH_PREFIX = '/Users/sn5/git/other/iConsent/video-generator/assets/logo/'
    SB_AUDIO_PATH_PREFIX = '/Users/sn5/git/other/iConsent/modules/assets/'
    SB_VIDEO_PATH_PREFIX = '/Users/sn5/git/other/iConsent/modules/assets/'
    LANG_PATH = '/Users/sn5/git/other/iConsent/modules/config/languages/'
    CONFIG_PATH = '/Users/sn5/git/other/iConsent/modules/config/'
    FONT_PATH = '/Users/sn5/git/other/iConsent/video-generator/assets/fonts/'
    SB_LOGO_PATH_PREFIX_WRITE = '/Users/sn5/git/other/iConsent/modules/assets/'


class ProductionConfig(Config):
    LOCAL = False
    SB_LOGO_PATH_PREFIX = '/var/task/assets/logo/'
    SB_LOGO_PATH_PREFIX_WRITE = '/tmp/'
    SB_AUDIO_PATH_PREFIX = '/tmp/'
    SB_VIDEO_PATH_PREFIX = '/tmp/'
    LANG_PATH = '/var/task/config/languages/'
    CONFIG_PATH = '/var/task/config/'
    FONT_PATH = '/var/task/assets/fonts/'
