from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from video import Video
import json
import os
import re

app = Flask(__name__)
CORS(app)


@app.route("/video", methods=['GET', 'POST'])
@cross_origin()
def video():
    input_map = request.get_json()
    print(input_map)
    with open("/var/task/config/images.json", "r") as read_file:
        image_map = json.load(read_file)
    with open("/var/task/config/" + input_map.get('language') + ".json", "r") as read_file:
        lang_map = json.load(read_file)
    video = Video(lang_map, input_map, image_map)
    url = video.get_video()
    res = {"url": url}
    return jsonify(res)


if __name__ == "__main__":
    app.run()
