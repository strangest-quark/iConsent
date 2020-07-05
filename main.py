from video import Video
import json

if __name__ == '__main__':
    with open("./config/images.json", "r") as read_file:
        image_map = json.load(read_file)
    with open("input.json", "r") as read_file:
        input_map = json.load(read_file)
    with open("./config/" + input_map.get('language') + ".json", "r") as read_file:
        lang_map = json.load(read_file)
    video = Video(lang_map, input_map, image_map)
    video.get_video()