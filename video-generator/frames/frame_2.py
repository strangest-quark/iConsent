import numpy as np
import math
import moviepy.editor as mpy
import PIL
from moviepy.editor import *
from gtts import gTTS
import os
from frames.text_generator.straight_text import straight_text
from googletrans import Translator
from PIL import Image
from PIL import ImageDraw

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

    def fill_text(self, text, iter):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start + 1:end]
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
            else:
                fill = k
            text = text[:start] + fill + text[end + 1:]
        if iter == 1:
            return self.translator.translate(text, dest=Frame2.lang_map.get('lan')).text.replace('(', '{').replace(')', '}')
        else:
            return text

    def concatenate_images(self, imgList):
        W, H = self.config.VIDEO_SIZE

        images = [Image.open(self.config.SB_LOGO_PATH_PREFIX + self.image_map.get(img)) for img in imgList]
        num_images = len(images)

        widths, heights = zip(*(i.size for i in images))

        total_width = int(max(widths) * 2)
        max_height = max(heights) * int(math.ceil(num_images/2))
        
        combined_image = Image.new('RGBA', (total_width, max_height), (0,0,0,0))
        
        x_offset = 0
        y_offset = 0

        if num_images % 2 == 0:
            for index, im in enumerate(images):
                print(im)
                if index % 2 == 0:
                    combined_image.paste(im, (x_offset, y_offset))
                    x_offset += im.size[0]
                else:
                    combined_image.paste(im, (x_offset, y_offset))
                    x_offset = 0
                    y_offset += im.size[1]
        else:
            for index in range(len(images) - 1):
                im = images[index]
                if index % 2 == 0:
                    combined_image.paste(im, (x_offset, y_offset))
                    x_offset += im.size[0]
                else:
                    combined_image.paste(im, (x_offset, y_offset))
                    x_offset = 0
                    y_offset += im.size[1]
                last_image = images[len(images) - 1]
                combined_image.paste(last_image, (int(x_offset + images[0].size[0]/2), y_offset))

        #Transparent background for odd number of fips
        # transparent_area = (50,80,100,200)
        # mask = Image.new('L', combined_image.size, color=255)
        # draw = ImageDraw.Draw(mask)
        # draw.rectangle(transparent_area, fill=0)
        # combined_image.putalpha(mask)
        combined_image.save(self.config.SB_LOGO_PATH_PREFIX + 'combined_banks.png')
        return combined_image


    def generate_video_part(self, txnId):
        if not self.config.LOCAL:
            os.chdir("/var/task/")
        W, H = self.config.VIDEO_SIZE
        bgImage = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + "bg_2.png")
        fipList = self.input_map.get("fip")
        
        fip_x_position = 0
        fip_y_position = 0
        fip_img_path = ''

        num_images_pow = pow(2, len(fipList))

        if len(fipList) == 1: 
            fip_x_position = W/4-self.config.BANK_ICON_SIZE/3
            fip_img_path = self.image_map.get(fipList[0])
            fip_y_position = H/4
        else:
            fip_x_position = W/6-self.config.BANK_ICON_SIZE/3
            fip_y_position = int(H/num_images_pow)
            self.concatenate_images(fipList)
            fip_img_path = 'combined_banks.png'

        height_final_image = self.config.BANK_ICON_SIZE * int(math.ceil(len(fipList)/2))

        fip_logo = mpy.ImageClip(self.config.SB_LOGO_PATH_PREFIX + fip_img_path). \
            set_position((fip_x_position, fip_y_position)).resize(height=height_final_image)
        self.text_to_speech(self.fill_text(self.fill_text(Frame2.lang_map.get('audio2'), 1), 2), Frame2.lang_map.get('lan'), txnId)
        audioclip = AudioFileClip(self.config.SB_AUDIO_PATH_PREFIX + "audio-" + txnId + "-2.mp3")
        Frame2.map['text2'] = self.fill_text(self.fill_text(Frame2.lang_map.get('text2'), 1), 2)
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
        os.remove(self.config.SB_LOGO_PATH_PREFIX_WRITE + 'combined_banks.png')
        return video, 2
