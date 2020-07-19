import time
import json
from config.config import DevelopmentConfig
from process import process

config = DevelopmentConfig

if __name__ == '__main__':
    with open(config.CONFIG_PATH + 'local_input.json', "r") as read_file:
        dashboard_obj = json.load(read_file)
    print(process(dashboard_obj))