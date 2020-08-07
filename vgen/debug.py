import time
import json
from vgen.worker import main
from vgen.config.config import DevelopmentConfig
from moviepy.editor import *
import uuid
from vgen.video.video import Video

config = DevelopmentConfig

if __name__ == '__main__':
    with open(config.CONFIG_PATH + 'images.json', "r") as read_file:
        config.image_map = json.load(read_file)
    with open(config.CONFIG_PATH + '/frames/frame_2.json', "r") as read_file:
        config.frame_map = json.load(read_file)
    with open(config.CONFIG_PATH + '/local_input.json', "r") as read_file:
        config.input_map = json.load(read_file)
    with open(config.LANG_PATH + config.input_map.get('language') + ".json", "r") as read_file:
        config.lang_map = json.load(read_file)
    video = Video(config)
    final_clip = concatenate_videoclips([video.generate_video_part('123')])
    final_clip.write_videofile(
        config.SB_VIDEO_PATH_PREFIX + config.input_map.get("fiu") + '-' + '123' + '-' + config.input_map.get(
            'language') + '.mp4', fps=10)
