from flask import Flask, request, Response
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
    input_map = {
        "fip": "Citibank",
        "fiu": "Mint",
        "datatype": "transactions",
        "account": "savings",
        "mode": "view",
        "type": "periodic",
        "language": "english"
    }
    print(input_map)
    with open("./config/images.json", "r") as read_file:
        image_map = json.load(read_file)
    with open("./config/" + input_map.get('language') + ".json", "r") as read_file:
        lang_map = json.load(read_file)
    video = Video(lang_map, input_map, image_map)
    video.get_video()
    full_path = "./assets/video/" + input_map.get("fiu") + '-' + input_map.get('language') + '.mp4'
    file_size = os.stat(full_path).st_size
    start = 0
    length = 10240  # can be any default length you want
    range_header = request.headers.get('Range', None)
    if range_header:
        m = re.search('([0-9]+)-([0-9]*)', range_header)  # example: 0-1000 or 1250-
        g = m.groups()
        byte1, byte2 = 0, None
        if g[0]:
            byte1 = int(g[0])
        if g[1]:
            byte2 = int(g[1])
        if byte1 < file_size:
            start = byte1
        if byte2:
            length = byte2 + 1 - byte1
        else:
            length = file_size - start
    with open(full_path, 'rb') as f:
        f.seek(start)
        chunk = f.read(length)
    rv = Response(chunk, 206, mimetype='video/mp4', content_type='video/mp4', direct_passthrough=True)
    rv.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(start, start + length - 1, file_size))
    return rv


@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    return response


if __name__ == "__main__":
    app.run()
