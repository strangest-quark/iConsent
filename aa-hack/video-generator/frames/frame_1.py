import moviepy.editor as mpy
from moviepy.editor import *
from gtts import gTTS
import os
from frames.text_generator.straight_text import straight_text
from googletrans import Translator


class Frame1(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame1.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config
        self.translator = Translator()

    def text_to_speech(self, text, lan, txnId):
        language = lan
        myobj = gTTS(text=text, lang=language, slow=False)
        if not self.config.LOCAL:
            os.chdir('/tmp')
        myobj.save(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + '-1.mp3')

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
                        fill = fill[:-1] + ' ' + Frame1.lang_map.get('and') + ' ' + Frame1.lang_map.get(ele)
                    else:
                        fill = fill + Frame1.lang_map.get(ele) + ','
                    i = i + 1
                if fill[-1] == ',':
                    fill = fill[:-1]
                text = text[:start] + fill + text[end + 1:]
                continue
            else:
                k = self.input_map.get(key)
            if k in Frame1.lang_map:
                fill = Frame1.lang_map.get(k)
            else:
                fill = k
            text = text[:start] + fill + text[end + 1:]
        if iter == 1 and Frame1.lang_map.get('lan') == 'en-IN':
            return text.replace('(', '{').replace(')', '}')
        if iter == 1:
            return self.translator.translate(text, dest=Frame1.lang_map.get('lan')).text.replace('(', '{').replace(')', '}')
        else:
            return text.capitalize()

    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + "bg_1.png")
        fiu_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("fiu"))). \
            set_position((W/2-150, H/5)).resize(height=self.config.ICON_SIZE)
        arrow_gif = VideoFileClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get("left_arrow")). \
            set_position((W/2-30, H/5)).resize(height=self.config.ICON_SIZE)
        account_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("account")[0])). \
            set_position((W/2+100, H/5)).resize(height=self.config.ICON_SIZE)
        self.text_to_speech(self.fill_text(self.fill_text(Frame1.lang_map.get('audio1'), 1), 2), Frame1.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + "-1.mp3")
        Frame1.map['text1'] = self.fill_text(self.fill_text(Frame1.lang_map.get('text1'), 1), 2)
        straight_text(Frame1.map['text1'], Frame1.lang_map.get('font'), Frame1.lang_map.get('fontsize1'), txnId, 1, self.config)
        text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-1-' + txnId+'.png')
        video = mpy.CompositeVideoClip(
            [
                bgImage,
                fiu_logo,
                arrow_gif,
                account_logo,
                text.set_position(('center', fiu_logo.size[1] + 40)),
            ],
            size=self.config.VIDEO_SIZE). \
            on_color(
            color=self.config.WHITE,
            col_opacity=1).set_duration(audioclip.duration)

        new_audioclip = CompositeAudioClip([audioclip])
        video.audio = new_audioclip
        os.remove(self.config.SB_AUDIO_PATH_PREFIX + 'audio-' + txnId + '-1.mp3')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-1-' + txnId+'.png')
        return video, 1