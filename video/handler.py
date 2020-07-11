import time
import json
from frame_1 import Frame1
from frame_2 import Frame2
from frame_3 import Frame3
from frame_4 import Frame4
from frame_5 import Frame5
from frame_6 import Frame6
from frame_7 import Frame7
from worker import main
from config.config import ProductionConfig
from moviepy.editor import *
import boto3
import uuid

config = ProductionConfig


def handler(event, context):
    # config
    config.input_map = event["req"]
    with open(config.CONFIG_PATH+'images.json', "r") as read_file:
        config.image_map = json.load(read_file)
    with open(config.LANG_PATH + config.input_map.get('language') + ".json", "r") as read_file:
        config.lang_map = json.load(read_file)

    # worker threads for frames
    video_obj_arr = []
    for i in range(1, 8):
        video_obj_arr.append(eval('Frame' + str(i))(config))
    _start = time.time()
    txnId = str(uuid.uuid4())
    out_queue = main(video_obj_arr, txnId)
    frames = list(out_queue.queue)
    frames.sort(key=lambda x: x[1])

    # final clip merge
    final_clip = concatenate_videoclips([frame[0] for frame in frames])
    final_clip.write_videofile(
        config.SB_VIDEO_PATH_PREFIX + config.input_map.get("fiu") + '-' + txnId + '-' + config.input_map.get('language') + '.mp4', fps=10)

    # s3 upload
    s3 = boto3.resource("s3")
    key = str(uuid.uuid4())
    s3.meta.client.upload_file(
        config.SB_VIDEO_PATH_PREFIX + config.input_map.get("fiu") + '-' + txnId + '-' + config.input_map.get(
            'language') + '.mp4', config.bucket_name, key + ".mp4")
    location = boto3.client('s3').get_bucket_location(Bucket=config.bucket_name)['LocationConstraint']

    #response
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, config.bucket_name, key + ".mp4")
    return url
