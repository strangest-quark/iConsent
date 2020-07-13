import moviepy.editor as mpy
from moviepy.editor import *
import gizeh as gz
from gtts import gTTS
import os
from frames.text_generator.calendar import calendar
from frames.text_generator.straight_text import straight_text
from googletrans import Translator



class Frame4(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame4.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config
        self.translator = Translator()

    def text_to_speech(self, text, lan, txnId):
        language = lan
        myobj = gTTS(text=text, lang=language, slow=False)
        if not self.config.LOCAL:
            os.chdir('/tmp')
        myobj.save(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + '-4.mp3')

    def fill_text(self, text):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start + 1:end]
            if self.input_map.get(key) in Frame4.lang_map:
                fill = Frame4.lang_map.get(self.input_map.get(key))
            elif Frame4.lang_map.get('lan') == 'en-IN':
                fill = self.input_map.get(key)
            else:
                fill = self.translator.translate(self.input_map.get(key), dest=Frame4.lang_map.get('lan')).text
            text = text[:start] + fill + text[end + 1:]
        return text.capitalize()

    @staticmethod
    def render_text4(t):
        WHITE_GIZEH = (1, 1, 1)
        BLUE = (59 / 255, 89 / 255, 152 / 255)
        surface = gz.Surface(640, 60, bg_color=WHITE_GIZEH)
        text = gz.text(Frame4.map.get('text4'), fontfamily=Frame4.lang_map.get('font'),
                       fontsize=Frame4.lang_map.get('fontsize'), fontweight='bold', fill=BLUE, xy=(320, 40))
        text.draw(surface)
        return surface.get_npimage()

    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        calendar(self.config, 'fiFrom', txnId)
        calendar(self.config, 'fiTo', txnId)
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + "bg_7.png")
        calendar_from_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'fiFrom-' + txnId + '.png'). \
            set_position((W / 2 - 170, H / 4)).resize(width=self.config.ICON_SIZE)
        calendar_to_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'fiTo-' + txnId + '.png'). \
            set_position((W / 2 + 80, H / 4)).resize(width=self.config.ICON_SIZE)
        self.text_to_speech(self.fill_text(Frame4.lang_map.get('audio4')), Frame4.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio" + '-' + txnId + "-4.mp3")
        Frame4.map['text4'] = self.fill_text(Frame4.lang_map.get('text4'))
        straight_text(Frame4.map['text4'], Frame4.lang_map.get('font'), Frame4.lang_map.get('fontsize7'), txnId, 4, self.config)
        text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE + '-text-4-' + txnId + '.png')
        video = mpy.CompositeVideoClip(
            [
                bgImage,
                calendar_from_logo,
                calendar_to_logo,
                text.set_position(('center', calendar_to_logo.size[1] + 20)),
            ],
            size=self.config.VIDEO_SIZE). \
            on_color(
            color=self.config.WHITE,
            col_opacity=1).set_duration(audioclip.duration)

        new_audioclip = CompositeAudioClip([audioclip])
        video.audio = new_audioclip
        os.remove(self.config.SB_AUDIO_PATH_PREFIX + 'audio-' + txnId + '-4.mp3')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + '-text-4-' + txnId + '.png')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'fiFrom-' + txnId + '.png')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'fiTo-' + txnId + '.png')
        return video, 4