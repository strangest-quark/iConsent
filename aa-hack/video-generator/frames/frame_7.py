import moviepy.editor as mpy
from moviepy.editor import *
from gtts import gTTS
import os
from frames.text_generator.calendar import calendar
from frames.text_generator.straight_text import straight_text
from googletrans import Translator


class Frame7(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame7.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config
        self.translator = Translator()

    def text_to_speech(self, text, lan, txnId):
        language = lan
        myobj = gTTS(text=text, lang=language, slow=False)
        if not self.config.LOCAL:
            os.chdir('/tmp')
        myobj.save(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + '-7.mp3')

    def fill_text(self, text, iter):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start + 1:end].lower()
            if key in self.config.static_keys:
                if iter == 1:
                    text = list(text)
                    text[start] = '('
                    text[end] = ')'
                    text = ''.join(text)
                    continue
            if isinstance(self.input_map.get(key), list):
                fill = ''
                i = 0
                for ele in self.input_map.get(key):
                    if len(self.input_map.get(key)) > 1 and i == len(self.input_map.get(key)) - 1:
                        fill = fill[:-1] + ' ' + Frame7.lang_map.get('and') + ' ' + Frame7.lang_map.get(ele)
                    else:
                        fill = fill + Frame7.lang_map.get(ele) + ','
                    i = i+1
                if fill[-1] == ',':
                    fill = fill[:-1]
                text = text[:start] + fill + text[end + 1:]
                continue
            else:
                k = self.input_map.get(key)
            if k in Frame7.lang_map:
                fill = Frame7.lang_map.get(k)
            else:
                fill = k
            text = text[:start] + fill + text[end + 1:]
        if iter == 1 and Frame7.lang_map.get('lan') == 'en-IN':
            return text.replace('(', '{').replace(')', '}')
        if iter == 1:
            return self.translator.translate(text, dest=Frame7.lang_map.get('lan')).text.replace('(', '{').replace(')', '}')
        else:
            return text.capitalize()


    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        calendar(self.config, 'consentfrom', txnId)
        calendar(self.config, 'consentto', txnId)
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + "bg_7.png")
        calendar_from_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'consentfrom-' + txnId + '.png'). \
            set_position((W/2-170, H/4)).resize(width=self.config.ICON_SIZE)
        calendar_to_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'consentto-' + txnId + '.png'). \
            set_position((W/2+80, H/4)).resize(width=self.config.ICON_SIZE)
        self.text_to_speech(self.fill_text(self.fill_text(Frame7.lang_map.get('audio7'), 1), 2), Frame7.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + "-7.mp3")
        Frame7.map['text7'] = self.fill_text(self.fill_text(Frame7.lang_map.get('text7'), 1), 2)
        straight_text(Frame7.map['text7'], Frame7.lang_map.get('font'), Frame7.lang_map.get('fontsize7'), txnId, 7, self.config)
        text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-7-' + txnId+'.png')
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
        os.remove(self.config.SB_AUDIO_PATH_PREFIX + 'audio-' + txnId + '-7.mp3')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-7-' + txnId+'.png')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'consentfrom-' + txnId + '.png')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'consentto-' + txnId + '.png')
        return video, 7