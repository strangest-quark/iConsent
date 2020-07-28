import time
import json
from frames.frame_1 import Frame1
from frames.frame_2 import Frame2
from frames.frame_3 import Frame3
from frames.frame_4 import Frame4
from frames.frame_5 import Frame5
from frames.frame_6 import Frame6
from frames.frame_7 import Frame7
from worker import main
from config.config import DevelopmentConfig
from moviepy.editor import *
import uuid

config = DevelopmentConfig

if __name__ == '__main__':
    with open(config.CONFIG_PATH + 'images.json', "r") as read_file:
        config.image_map = json.load(read_file)
    with open(config.CONFIG_PATH + 'local_input.json', "r") as read_file:
        config.input_map = json.load(read_file)
    with open(config.LANG_PATH + config.input_map.get('language') + ".json", "r") as read_file:
        config.lang_map = json.load(read_file)
    video_obj_arr = []
    for i in range(1, 8):
        if i == 6 and config.input_map.get('mode') != 'store':
            continue
        else:
            video_obj_arr.append(eval('Frame' + str(i))(config))
    _start = time.time()
    txnId = str(uuid.uuid4())
    out_queue = main(video_obj_arr, txnId, len(video_obj_arr)+1)
    frames = list(out_queue.queue)
    frames.sort(key=lambda x: x[1])
    print(frames)
    final_clip = concatenate_videoclips([frame[0] for frame in frames])
    final_clip.write_videofile(
        config.SB_VIDEO_PATH_PREFIX + config.input_map.get("fiu") + '-' + txnId + '-' + config.input_map.get(
            'language') + '.mp4', fps=10)
