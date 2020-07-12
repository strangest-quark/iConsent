import moviepy.editor as mpy
from moviepy.editor import *
import gizeh as gz
from gtts import gTTS
import os
from frames.text_generator.calendar import calendar
from frames.text_generator.straight_text import straight_text


class Frame7(object):
    map = dict()
    lang_map = dict()

    def __init__(self, config):
        Frame7.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config

    def text_to_speech(self, text, lan, txnId):
        language = lan
        myobj = gTTS(text=text, lang=language, slow=False)
        if not self.config.LOCAL:
            os.chdir('/tmp')
        myobj.save(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + '-7.mp3')

    def fill_text(self, text):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start + 1:end]
            if self.input_map.get(key) in Frame7.lang_map:
                fill = Frame7.lang_map.get(self.input_map.get(key))
            else:
                fill = self.input_map.get(key)
            text = text[:start] + fill + text[end + 1:]
        return text.capitalize()

    @staticmethod
    def render_text7(t):
        WHITE_GIZEH = (1, 1, 1)
        BLUE = (59 / 255, 89 / 255, 152 / 255)
        surface = gz.Surface(640, 60, bg_color=WHITE_GIZEH)
        text = gz.text(Frame7.map.get('text7'), fontfamily=Frame7.lang_map.get('font'),
                       fontsize=Frame7.lang_map.get('fontsize'), fontweight='bold', fill=BLUE, xy=(320, 40))
        text.draw(surface)
        return surface.get_npimage()

    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        calendar(self.config, 'consentFrom', txnId)
        calendar(self.config, 'consentTo', txnId)
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + "bg_7.png")
        calendar_from_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'consentFrom-' + txnId + '.png'). \
            set_position((W/2-200, H/5)).resize(width=150)
        calendar_to_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'consentTo-' + txnId + '.png'). \
            set_position((W/2+50, H/5)).resize(width=150)
        self.text_to_speech(self.fill_text(Frame7.lang_map.get('audio7')), Frame7.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio" + '-' + txnId + "-7.mp3")
        Frame7.map['text7'] = self.fill_text(Frame7.lang_map.get('text7'))
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
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'consentFrom-' + txnId + '.png')
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'consentTo-' + txnId + '.png')
        return video, 7