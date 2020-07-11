import moviepy.editor as mpy
from moviepy.editor import *
import gizeh as gz
from gtts import gTTS
import os


class Frame3(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame3.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config

    def text_to_speech(self, text, lan, txnId):
        language = lan
        myobj = gTTS(text=text, lang=language, slow=False)
        if not self.config.LOCAL:
            os.chdir('/tmp')
        myobj.save(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + '-3.mp3')

    def fill_text(self, text):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start + 1:end]
            if self.input_map.get(key) in Frame3.lang_map:
                fill = Frame3.lang_map.get(self.input_map.get(key))
            else:
                fill = self.input_map.get(key)
            text = text[:start] + fill + text[end + 1:]
        return text.capitalize()

    @staticmethod
    def render_text3(t):
        WHITE_GIZEH = (1, 1, 1)
        BLUE = (59 / 255, 89 / 255, 152 / 255)
        surface = gz.Surface(640, 60, bg_color=WHITE_GIZEH)
        text = gz.text(Frame3.map.get('text3'), fontfamily=Frame3.lang_map.get('font'),
                       fontsize=Frame3.lang_map.get('fontsize'), fontweight='bold', fill=BLUE, xy=(320, 40))
        text.draw(surface)
        return surface.get_npimage()

    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        mode_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("type"))). \
            set_position((150, 40)).resize(height=100)
        data_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("datatype"))). \
            set_position((350, 40)).resize(height=100)
        self.text_to_speech(self.fill_text(Frame3.lang_map.get('audio3')), Frame3.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio" + '-' + txnId + "-3.mp3")
        Frame3.map['text3'] = self.fill_text(Frame3.lang_map.get('text3'))
        text = mpy.VideoClip(self.render_text3, duration=self.config.DURATION)
        video = mpy.CompositeVideoClip(
            [
                mode_logo,
                data_logo,
                text.set_position(('center', mode_logo.size[1] + 40)),
            ],
            size=self.config.VIDEO_SIZE). \
            on_color(
            color=self.config.WHITE,
            col_opacity=1).set_duration(audioclip.duration)
        new_audioclip = CompositeAudioClip([audioclip])
        video.audio = new_audioclip
        os.remove(self.config.SB_AUDIO_PATH_PREFIX + 'audio-' + txnId + '-3.mp3')
        return video, 3