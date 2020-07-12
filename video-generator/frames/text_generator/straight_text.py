from PIL import Image, ImageDraw, ImageFont

def straight_text(text, font, fontsize, txnId, i):
    img = Image.new('RGBA', (640, 200), (255, 0, 0, 0))
    W, H = img.size
    draw = ImageDraw.Draw(img)
    msg1 = text
    font1 = ImageFont.truetype('/Users/sn5/git/other/iConsent/video-generator/assets/fonts/'+font+'.ttf',
                               fontsize)
    w, h = draw.textsize(msg1, font=font1)
    draw.text(((W-w)/2, (H-h)/2), msg1, (0, 0, 0), font=font1)
    img.save('/Users/sn5/git/other/iConsent/video-generator/assets/logo/'+'-text-'+str(i)+'-'+txnId+'.png', 'PNG')
