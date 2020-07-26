from PIL import Image, ImageDraw, ImageFont
import sys

def calendar(config, key, txnId):
    img = Image.open(config.SB_LOGO_PATH_PREFIX+key+'.png')
    W, H = img.size
    draw = ImageDraw.Draw(img)
    msg1 = config.input_map[key].split('-')[0]
    msg2 = config.input_map[key].split('-')[2][0:2]
    msg3 = config.lang_map[config.input_map[key].split('-')[1]]
    font1 = ImageFont.truetype(config.FONT_PATH+'OpenSans-ExtraBold.ttf', 175)
    font2 = ImageFont.truetype(config.FONT_PATH+'OpenSans-ExtraBold.ttf', 500)
    font3 = ImageFont.truetype(config.FONT_PATH+config.lang_map['font']+'.ttf', config.lang_map['calendar_font_size'])
    w, h = draw.textsize(msg1, font=font1)
    draw.text(((W-w)/2, 200), msg1, (255, 255, 255), font=font1)
    w, h = draw.textsize(msg2, font=font2)
    draw.text(((W-w)/2, (H-h)/2-50), msg2, (0, 0, 0), font=font2)
    w, h = draw.textsize(msg3, font=font3)
    draw.text(((W-w)/2, (H-h)-280), msg3, (0, 0, 0), font=font3)
    img.save(config.SB_LOGO_PATH_PREFIX_WRITE+key+'-'+txnId+'.png')
