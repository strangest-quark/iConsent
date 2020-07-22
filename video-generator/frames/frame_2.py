import moviepy.editor as mpy
from moviepy.editor import *
from gtts import gTTS
import os
from frames.text_generator.straight_text import straight_text
from googletrans import Translator


class Frame2(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame2.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config
        self.translator = Translator()

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
            if isinstance(self.input_map.get(key), list):
                fill = ''
                i = 0
                for ele in self.input_map.get(key):
                    if len(self.input_map.get(key)) > 1 and i == len(self.input_map.get(key)) - 1:
                        fill = fill[:-1] + ' ' + Frame2.lang_map.get('and') + ' ' + Frame2.lang_map.get(ele)
                    else:
                        fill = fill + Frame2.lang_map.get(ele) + ','
                    i = i+1
                if fill[-1] == ',':
                    fill = fill[:-1]
                text = text[:start] + fill + text[end + 1:]
                continue
            else:
                k = self.input_map.get(key)
            if k in Frame2.lang_map:
                fill = Frame2.lang_map.get(k)
            elif Frame2.lang_map.get('lan') == 'en-IN':
                fill = k
            else:
                fill = self.translator.translate(k, dest=self.Frame2.lang_map.get('lan')).text
            text = text[:start] + fill + text[end + 1:]
        return text.capitalize()


    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + "bg_2.png")
        fip_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("fip")[0])). \
            set_position((W/4-self.config.BANK_ICON_SIZE/3, H/3)).resize(height=self.config.BANK_ICON_SIZE)
        self.text_to_speech(self.fill_text(Frame2.lang_map.get('audio2')), Frame2.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio" + '-' + txnId + "-2.mp3")
        Frame2.map['text2'] = self.fill_text(Frame2.lang_map.get('text2'))
        straight_text(Frame2.map['text2'], Frame2.lang_map.get('font'), Frame2.lang_map.get('fontsize2'), txnId, 2, self.config)
        text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-2-' + txnId+'.png')
        video = mpy.CompositeVideoClip(
            [
                bgImage,
                fip_logo,
                text.set_position((W/5+50, H/5)),
            ],
            size=self.config.VIDEO_SIZE). \
            on_color(
            color=self.config.WHITE,
            col_opacity=1).set_duration(audioclip.duration)
        new_audioclip = CompositeAudioClip([audioclip])
        video.audio = new_audioclip
        os.remove(self.config.SB_AUDIO_PATH_PREFIX + 'audio-' + txnId + '-2.mp3')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-2-' + txnId+'.png')
        return video, 2
