import moviepy.editor as mpy
from moviepy.editor import *
import os
from vgen.image.text_image import straight_text
from vgen.audio.text_to_speech import TextToSpeech
from vgen.text.fill_text import FillText
from googletrans import Translator

class Video(object):

    def __init__(self, config):
        self.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.frame_map = config.frame_map
        self.config = config
        self.translator = Translator()
        self.fill_text = FillText(config)
        self.text_to_speech = TextToSpeech(config)

    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.config.frame_map['bg'])
        fiu_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("fiu"))). \
            set_position((W / 2 - 150, H / 5)).resize(height=self.config.ICON_SIZE)
        arrow_gif = VideoFileClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get("left_arrow")). \
            set_position((W / 2 - 30, H / 5)).resize(height=self.config.ICON_SIZE)
        account_logo = mpy.ImageClip(
            self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(self.input_map.get("account")[0])). \
            set_position((W / 2 + 100, H / 5)).resize(height=self.config.ICON_SIZE)
        self.text_to_speech.text_to_speech(self.fill_text.fill_text(self.fill_text.fill_text(self.frame_map.get('audio'), 1), 2), self.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + "-1.mp3")
        self.frame_map['text'] = self.fill_text.fill_text(self.fill_text.fill_text(self.frame_map.get('text'), 1), 2)
        straight_text(self.config.frame_map['text'], self.lang_map.get('font'), self.lang_map.get('fontsize'), txnId, 1, self.config)
        text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE + '-text-1-' + txnId + '.png')
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
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + '-text-1-' + txnId + '.png')
        return video
