import moviepy.editor as mpy
from moviepy.editor import *
import gizeh as gz
from gtts import gTTS
import os
from frames.text_generator.straight_text import straight_text


class Frame1(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame1.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config

    def text_to_speech(self, text, lan, txnId):
        language = lan
        myobj = gTTS(text=text, lang=language, slow=False)
        if not self.config.LOCAL:
            os.chdir('/tmp')
        myobj.save(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + '-1.mp3')

    def fill_text(self, text):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start + 1:end]
            if self.input_map.get(key) in Frame1.lang_map:
                fill = Frame1.lang_map.get(self.input_map.get(key))
            else:
                fill = self.input_map.get(key)
            text = text[:start] + fill + text[end + 1:]
        return text.capitalize()

    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        fiu_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("fiu"))). \
            set_position((W/2-200, H/5)).resize(width=200)
        account_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("account"))). \
            set_position((W/2+50, H/5)).resize(width=100)
        self.text_to_speech(self.fill_text(Frame1.lang_map.get('audio1')), Frame1.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + "-1.mp3")
        Frame1.map['text1'] = self.fill_text(Frame1.lang_map.get('text1'))
        straight_text(Frame1.map['text1'], Frame1.lang_map.get('font'), Frame1.lang_map.get('fontsize1'), txnId, 1, self.config)
        text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE+'-text-1-' + txnId+'.png')
        video = mpy.CompositeVideoClip(
            [
                fiu_logo,
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