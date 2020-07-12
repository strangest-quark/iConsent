import moviepy.editor as mpy
from moviepy.editor import *
import gizeh as gz
from gtts import gTTS
import os
from frames.text_generator.straight_text import straight_text


class Frame2(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame2.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config

    def text_to_speech(self, text, lan, txnId):
        language = lan
        myobj = gTTS(text=text, lang=language, slow=False)
        if not self.config.LOCAL:
            os.chdir('/tmp')
        myobj.save(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + '-2.mp3')

    def fill_text(self, text):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start + 1:end]
            if self.input_map.get(key) in Frame2.lang_map:
                fill = Frame2.lang_map.get(self.input_map.get(key))
            else:
                fill = self.input_map.get(key)
            text = text[:start] + fill + text[end + 1:]
        return text.capitalize()

    @staticmethod
    def render_text2(t):
        WHITE_GIZEH = (1, 1, 1)
        BLUE = (59 / 255, 89 / 255, 152 / 255)
        surface = gz.Surface(640, 60, bg_color=WHITE_GIZEH)
        text = gz.text(Frame2.map.get('text2'), fontfamily=Frame2.lang_map.get('font'),
                       fontsize=Frame2.lang_map.get('fontsize'), fontweight='bold', fill=BLUE, xy=(320, 40))
        text.draw(surface)
        return surface.get_npimage()

    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        fip_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("fip"))). \
            set_position((W/2-150, H/5)).resize(height=100)
        self.text_to_speech(self.fill_text(Frame2.lang_map.get('audio2')), Frame2.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio" + '-' + txnId + "-2.mp3")
        Frame2.map['text2'] = self.fill_text(Frame2.lang_map.get('text2'))
        straight_text(Frame2.map['text2'], Frame2.lang_map.get('font'), Frame2.lang_map.get('fontsize2'), txnId, 2)
        text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX+'-text-2-' + txnId+'.png')
        video = mpy.CompositeVideoClip(
            [
                fip_logo,
                text.set_position(('center', fip_logo.size[1] + 40)),
            ],
            size=self.config.VIDEO_SIZE). \
            on_color(
            color=self.config.WHITE,
            col_opacity=1).set_duration(audioclip.duration)
        new_audioclip = CompositeAudioClip([audioclip])
        video.audio = new_audioclip
        os.remove(self.config.SB_AUDIO_PATH_PREFIX + 'audio-' + txnId + '-2.mp3')
        os.remove(self.config.SB_LOGO_PATH_PREFIX+'-text-2-' + txnId+'.png')
        return video, 2
