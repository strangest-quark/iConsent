import moviepy.editor as mpy
# TODO: import only necessary ones
from moviepy.editor import *
import os
from modules.image.text_image import straight_text
from modules.audio.text_to_speech import TextToSpeech
from modules.text.fill_text import FillText
from modules.image.grid_image import grid_image
from googletrans import Translator


class Video(object):

    def __init__(self, config):
        self.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.frame_map = config.frame_map
        self.config = config
        self.fill_text = FillText(config)
        self.text_to_speech = TextToSpeech(config)

    # TODO: add key to saved content - like audio-txnId-1.mp3
    def generate_video_part(self, txnId):
        audioclip = None
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + self.config.frame_map['bg'])
        # Image content
        if 'imageGroup' in self.frame_map:
            video_arr = [bgImage] + self.image_part(txnId)
        # Text content
        if 'text' in self.frame_map:
            self.frame_map['text'] = self.fill_text.fill_text(self.fill_text.fill_text(self.frame_map.get('text'), 1),
                                                              2)
            straight_text(self.config.frame_map['text'], self.lang_map.get('font'), self.lang_map.get('fontsize'),
                          txnId, self.config)
            text = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'text-' + txnId + '.png')
            video_arr.append(text.set_position(('center', video_arr[-1].size[1] + 40)))
        # Audio content
        if 'audio' in self.frame_map:
            self.text_to_speech.text_to_speech(
                self.fill_text.fill_text(self.fill_text.fill_text(self.frame_map.get('audio'), 1), 2),
                self.lang_map.get('lan'), txnId)
            audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + "-1.mp3")
            new_audioclip = CompositeAudioClip([audioclip])

        if audioclip is not None:
            video_duration = audioclip.duration
        else:
            video_duration = self.config.DEFAULT_FRAME_DURATION
        video = mpy.CompositeVideoClip(video_arr, size=self.config.VIDEO_SIZE). \
            on_color(color=self.config.WHITE, col_opacity=1). \
            set_duration(video_duration)
        if audioclip is not None:
            video.audio = new_audioclip
        #os.remove(self.config.SB_AUDIO_PATH_PREFIX + 'audio-' + txnId + '-1.mp3')
        #os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'text-' + txnId + '.png')
        return video

    def image_part(self, txnId):
        W, H = self.config.VIDEO_SIZE
        span_len = len(self.config.frame_map['imageGroup']) - 1
        image_parts = []
        if self.config.frame_map['type'] == 'span':
            for idx, img in enumerate(self.config.frame_map['imageGroup']):
                if img.endswith('png') or img.endswith('jpeg') or img.endswith('png'):
                    image_parts.append(mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + img). \
                                       set_position((W / 2 + self.config.span[span_len][idx][0], H / 5 + \
                                                     self.config.span[span_len][idx][1])). \
                                       resize(height=self.config.ICON_SIZE))
                elif img.endswith('gif'):
                    image_parts.append(VideoFileClip(self.config.SB_LOGO_PATH_PREFIX + self.image_map. \
                                                     get(self.input_map.get("fiu"))). \
                                       set_position((W / 2 + self.config.span[span_len][idx][0], H / 5 + \
                                                     self.config.span[span_len][idx][1])). \
                                       resize(height=self.config.ICON_SIZE))
                # TODO: Handle error here for other image types
        elif self.config.frame_map['type'] == 'grid':
            combined_image, x_pos, y_pos, height = grid_image(self.config.frame_map['imageGroup'], self.config)
            img_path = self.config.SB_LOGO_PATH_PREFIX_WRITE + txnId + '-grid.png'
            combined_image.save(img_path)
            image_parts.append(mpy.ImageClip(img_path). \
                               set_position((x_pos, y_pos)).resize(height=height))
        return image_parts
