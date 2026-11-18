from PIL import Image, ImageDraw, ImageFont
import sys
FONT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/EBGaramond.ttf'
BG=(242,228,1,255); FG=(11,4,4,255); W=408
def render(ch,S=512,scale=4):
    N=S*scale
    f=ImageFont.truetype(FONT,100*scale); f.set_variation_by_axes([W])
    hb=f.getbbox('H'); size=100*scale*(236*scale/(hb[3]-hb[1]))
    f=ImageFont.truetype(FONT,int(size)); f.set_variation_by_axes([W])
    hb=f.getbbox('H'); top=138*scale-hb[1]
    im=Image.new('RGBA',(N,N),BG); d=ImageDraw.Draw(im)
    b=f.getbbox(ch); x=(N-(b[2]-b[0]))/2-b[0]
    d.text((x,top),ch,font=f,fill=FG)
    return im.resize((S,S),Image.LANCZOS)
s=render('S')
s.save('assets/images/icon-512.png')
s.save('favicon.ico',sizes=[(16,16),(32,32),(48,48),(256,256)])
