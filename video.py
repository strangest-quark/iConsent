import moviepy.editor as mpy
from moviepy.editor import *
import gizeh as gz
from gtts import gTTS
import os
import boto3
import uuid

VIDEO_SIZE = (640, 240)
BLUE = (59 / 255, 89 / 255, 152 / 255)
GREEN = (176 / 255, 210 / 255, 63 / 255)
WHITE = (255, 255, 255)
WHITE_GIZEH = (1, 1, 1)
SB_LOGO_PATH_PREFIX = '/var/task/assets/logo/'
SB_AUDIO_PATH_PREFIX = '/tmp/'
SB_VIDEO_PATH_PREFIX = '/tmp/'
DURATION = 5


class Video:
    map = dict()
    lang_map = dict()

    def __init__(self, lang_map, input_map, image_map):
        Video.lang_map = lang_map
        self.input_map = input_map
        self.image_map = image_map
        self.map = dict()

    def text_to_speech(self, text, index, lan):
        language = lan
        myobj = gTTS(text=text, lang=language, slow=False)
        os.chdir('/tmp')
        myobj.save(SB_AUDIO_PATH_PREFIX+"audio-" + str(index) + '.mp3')

    def fill_text(self, text):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start+1:end]
            text = text[:start] + Video.lang_map.get(self.input_map.get(key)) + text[end+1:]
        print(text)
        return text.capitalize()

    @staticmethod
    def render_text(t):
        surface = gz.Surface(640, 60, bg_color=WHITE_GIZEH)
        text = gz.text(Video.map.get('current_text'), fontfamily=Video.lang_map.get('font'),
                       fontsize=Video.lang_map.get('fontsize'), fontweight='bold', fill=BLUE, xy=(320, 40))
        text.draw(surface)
        return surface.get_npimage()

    def generate_video_part_1(self):
        fiu_logo = mpy.ImageClip(SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("fiu"))). \
            set_position((40, 40)).resize(width=200)
        double_arrow = mpy.ImageClip(SB_LOGO_PATH_PREFIX + self.image_map.get("double arrow")). \
            set_position((270, 50)).resize(height=50)
        fip_logo = mpy.ImageClip(SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("fip"))). \
            set_position((350, 40)).resize(width=200)
        self.text_to_speech(self.fill_text(Video.lang_map.get('audio1')), 1, Video.lang_map.get('lan'))
        audioclip = AudioFileClip(SB_AUDIO_PATH_PREFIX+"audio-1.mp3")
        Video.map['current_text'] = self.fill_text(Video.lang_map.get('text1'))
        text = mpy.VideoClip(self.render_text, duration=DURATION)
        video = mpy.CompositeVideoClip(
            [
                fiu_logo,
                double_arrow,
                fip_logo,
                text.set_position(('center', fiu_logo.size[1] + 40)),
            ],
            size=VIDEO_SIZE). \
            on_color(
            color=WHITE,
            col_opacity=1).set_duration(audioclip.duration)

        new_audioclip = CompositeAudioClip([audioclip])
        video.audio = new_audioclip
        os.chdir('/tmp')
        video.write_videofile(SB_VIDEO_PATH_PREFIX+self.input_map.get("fiu")+'-1.mp4', fps=10)
        return video

    def generate_video_part_2(self):
        os.chdir("/var/task/")
        type_logo = mpy.ImageClip(SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("type"))). \
            set_position((150, 40)).resize(height=100)
        data_logo = mpy.ImageClip(SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("datatype"))). \
            set_position((350, 40)).resize(height=100)
        self.text_to_speech(self.fill_text(Video.lang_map.get('audio2')), 2, Video.lang_map.get('lan'))
        audioclip = AudioFileClip(SB_AUDIO_PATH_PREFIX+"audio-2.mp3")
        Video.map['current_text'] = self.fill_text(Video.lang_map.get('text2'))
        print(Video.map['current_text'])
        text = mpy.VideoClip(self.render_text, duration=DURATION)
        video = mpy.CompositeVideoClip(
            [
                type_logo,
                data_logo,
                text.set_position(('center', type_logo.size[1] + 40)),
            ],
            size=VIDEO_SIZE). \
            on_color(
            color=WHITE,
            col_opacity=1).set_duration(audioclip.duration)
        new_audioclip = CompositeAudioClip([audioclip])
        video.audio = new_audioclip
        os.chdir('/tmp')
        video.write_videofile(SB_VIDEO_PATH_PREFIX+self.input_map.get("fiu") + '-2.mp4', fps=10)
        return video

    def get_video(self):
        self.generate_video_part_1()
        self.generate_video_part_2()
        video1 = VideoFileClip(SB_VIDEO_PATH_PREFIX+self.input_map.get("fiu")+'-1.mp4')
        video2 = VideoFileClip(SB_VIDEO_PATH_PREFIX+self.input_map.get("fiu")+'-2.mp4')
        final_clip = concatenate_videoclips([video1, video2])
        final_clip.write_videofile(SB_VIDEO_PATH_PREFIX + self.input_map.get("fiu") + '-' + self.input_map.get('language') + '.mp4')
        s3 = boto3.resource("s3")
        bucket_name = "iconsent-video"
        key = str(uuid.uuid4())
        s3.meta.client.upload_file(SB_VIDEO_PATH_PREFIX + self.input_map.get("fiu") + '-' + self.input_map.get('language') + '.mp4', bucket_name, key+".mp4")
        location = boto3.client('s3').get_bucket_location(Bucket=bucket_name)['LocationConstraint']
        url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, key+".mp4")
        os.remove(SB_VIDEO_PATH_PREFIX+self.input_map.get("fiu")+'-1.mp4')
        os.remove(SB_VIDEO_PATH_PREFIX+self.input_map.get("fiu")+'-2.mp4')
        os.remove(SB_AUDIO_PATH_PREFIX+'audio-1.mp3')
        os.remove(SB_AUDIO_PATH_PREFIX+'audio-2.mp3')
        return url
