import moviepy.editor as mpy
from moviepy.editor import *
from gtts import gTTS
import os
from frames.text_generator.straight_text import straight_text
from googletrans import Translator


class Frame3(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame3.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config
        self.translator = Translator()

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
            if isinstance(self.input_map.get(key), list):
                fill = ''
                i = 0
                for ele in self.input_map.get(key):
                    if len(self.input_map.get(key)) > 1 and i == len(self.input_map.get(key)) - 1:
                        fill = fill[:-1] + ' ' + Frame3.lang_map.get('and') + ' ' + Frame3.lang_map.get(ele)
                    else:
                        fill = fill + Frame3.lang_map.get(ele) + ','
                    i = i+1
                if fill[-1] == ',':
                    fill = fill[:-1]
                text = text[:start] + fill + text[end + 1:]
                continue
            else:
                k = self.input_map.get(key)
            if k in Frame3.lang_map:
                fill = Frame3.lang_map.get(k)
            elif Frame3.lang_map.get('lan') == 'en-IN':
                fill = k
            else:
                fill = self.translator.translate(k, dest=Frame3.lang_map.get('lan')).text
            text = text[:start] + fill + text[end + 1:]
        return text.capitalize()

    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + "bg_3.png")
        phone_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get('phone')).\
            set_position((W/2-self.config.ICON_SIZE*2, H/5)).resize(height=self.config.ICON_SIZE)
        if 'gif' in self.image_map.get(self.input_map.get('mode')):
            mode_logo = VideoFileClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get('mode'))). \
                set_position((W/2-self.config.ICON_SIZE/2, H/5)).resize(height=self.config.ICON_SIZE)
        else:
            mode_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get('mode'))). \
                set_position((W / 2 - self.config.ICON_SIZE / 2, H / 5)).resize(height=self.config.ICON_SIZE)
        data_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(','.join(self.input_map.get("datatype")))).\
            set_position((W/2+self.config.ICON_SIZE, H/5)).resize(height=self.config.ICON_SIZE)
        self.text_to_speech(self.fill_text(Frame3.lang_map.get('audio3')), Frame3.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio" + '-' + txnId + "-3.mp3")
        Frame3.map['text3'] = self.fill_text(Frame3.lang_map.get('text3'))
        straight_text(Frame3.map['text3'], Frame3.lang_map.get('font'), Frame3.lang_map.get('fontsize3'), txnId, 3, self.config)
        text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-3-' + txnId+'.png')
        video = mpy.CompositeVideoClip(
            [
                bgImage,
                phone_logo,
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
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-3-' + txnId+'.png')
        return video, 3