import moviepy.editor as mpy
from moviepy.editor import *
import gizeh as gz
from gtts import gTTS
import os
from frames.text_generator.straight_text import straight_text
from googletrans import Translator


class Frame6(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame6.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config
        self.translator = Translator()

    def text_to_speech(self, text, lan, txnId):
        language = lan
        myobj = gTTS(text=text, lang=language, slow=False)
        if not self.config.LOCAL:
            os.chdir('/tmp')
        myobj.save(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + '-6.mp3')

    def fill_text(self, text):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start + 1:end]
            if self.input_map.get(key) in Frame6.lang_map:
                fill = Frame6.lang_map.get(self.input_map.get(key))
            elif Frame6.lang_map.get('lan') == 'en-IN':
                fill = self.input_map.get(key)
            else:
                fill = self.translator.translate(self.input_map.get(key), dest=Frame6.lang_map.get('lan')).text
            text = text[:start] + fill + text[end + 1:]
        return text.capitalize()

    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + "bg_6.png")
        mode_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("mode"))). \
            set_position((W/2-50, H/5)).resize(width=self.config.ICON_SIZE)
        self.text_to_speech(self.fill_text(Frame6.lang_map.get('audio6')), Frame6.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio" + '-' + txnId + "-6.mp3")
        Frame6.map['text6'] = self.fill_text(Frame6.lang_map.get('text6'))
        straight_text(Frame6.map['text6'], Frame6.lang_map.get('font'), Frame6.lang_map.get('fontsize6'), txnId, 6, self.config)
        text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-6-' + txnId+'.png')
        video = mpy.CompositeVideoClip(
            [
                bgImage,
                mode_logo,
                text.set_position(('center', mode_logo.size[1] + 40)),
            ],
            size=self.config.VIDEO_SIZE). \
            on_color(
            color=self.config.WHITE,
            col_opacity=1).set_duration(audioclip.duration)

        new_audioclip = CompositeAudioClip([audioclip])
        video.audio = new_audioclip
        os.remove(self.config.SB_AUDIO_PATH_PREFIX + 'audio-' + txnId + '-6.mp3')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-6-' + txnId+'.png')
        return video, 6