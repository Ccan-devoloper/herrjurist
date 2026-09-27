#!/usr/bin/env python3
"""30 fps limited-animation cels from matching generated poses. No type overlays."""
import argparse
import json
import math
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

ROOT=Path(__file__).resolve().parent
W,H,FPS=941,1672,30

def source(name):
    p=ROOT/'masters'/f'{name}.jpg'
    if not p.exists():p=ROOT.parent/'reel-2026-09-30-v4'/'masters'/f'{name}.jpg'
    return Image.open(p).convert('RGB')

def soft_rect(box,r=14):
    m=Image.new('L',(W,H));ImageDraw.Draw(m).rectangle(box,fill=255)
    return m.filter(ImageFilter.GaussianBlur(r))

def soft_ellipse(box,r=12):
    m=Image.new('L',(W,H));ImageDraw.Draw(m).ellipse(box,fill=255)
    return m.filter(ImageFilter.GaussianBlur(r))

def edit(base,changed,mask,v):
    if v<=0:return base.copy()
    mask=mask.point(lambda x:round(x*min(1,v)))
    return Image.composite(changed,base,mask)

def window(t,a,b,c,d):
    """A small expression rises, holds, and settles in the locked frame."""
    if t<a or t>=d:return 0.
    if t<b:return (t-a)/(b-a)
    if t<c:return 1.
    return (d-t)/(d-c)

def cut(im,scale,center):
    cw,ch=round(W/scale),round(H/scale)
    x=max(0,min(W-cw,round(center[0]-cw/2)))
    y=max(0,min(H-ch,round(center[1]-ch/2)))
    return im.crop((x,y,x+cw,y+ch)).resize((W,H),Image.Resampling.LANCZOS)

def render_frame(t,T,A,M):
    b=T['boundaries']; intro=b[1]; interrogation=b[2]; sleepy=b[3]
    statement=b[4]; norm_end=b[5]; consent_end=b[6]
    if t<intro:
        im=A['01-consent']
        # The red rejection appears in the generated recorder, while the paper
        # remains the SAME signed document from first to last frame.
        v=min(1,max(0,(t-T['scanner_at'])/.20))
        im=edit(im,A['01-reject'],M['scanner'],v)
        im=edit(im,A['01-reject'],M['brakk_face'],1 if t>=T['scanner_at'] else 0)
        return im
    if t<interrogation:
        im=A['02-interrogation']
        if t<intro+.70:
            return cut(im,1.8,(580,258)) # one motivated rewind clock insert
        # Brakk briefly stops talking and clenches his jaw in the same shot.
        im=edit(im,A['04-statement'],M['brakk_expression'],window(t,4.63,4.75,5.22,5.36))
        return im
    if t<sleepy:
        im=A['02-interrogation']
        clock=min(1,max(0,(t-interrogation-.12)/.25))
        im=edit(im,A['02-later-tired'],M['clock'],clock)
        blink=min(1,max(0,(t-interrogation-.62)/.20))
        im=edit(im,A['02-later-tired'],M['zylla_face'],blink)
        # A matching generated cel moves Brakk's face, shoulder and glove.
        im=Image.blend(im,A['02-brakk-tense'],window(t,6.89,7.04,8.25,8.48))
        # Zylla struggles to keep an eye open, then closes it again.
        im=edit(im,A['02-interrogation'],M['zylla_eyes'],window(t,8.11,8.17,8.30,8.38))
        if t>interrogation+.94:
            return cut(im,1.16,(695,790)) # the fatigue close-up has a reason
        return im
    hit=T['table_at']
    if t<hit:
        im=edit(A['02-interrogation'],A['02-later-tired'],M['clock'],1)
        return edit(im,A['02-later-tired'],M['zylla_face'],1)
    if t<hit+.38:
        if t<hit+.067:return ImageEnhance.Brightness(A['03-slam']).enhance(1.19)
        return A['03-slam']
    if t<statement:
        im=A['04-statement']
        # Zylla's mouth and gaze follow the words picked up by the recorder.
        v=max(window(t,10.55,10.69,11.12,11.29),
              window(t,11.78,11.91,12.42,12.60))
        im=Image.blend(im,A['04-zylla-glance'],v)
        if t>statement-.72:return cut(im,1.43,(175,1255))
        return im
    if t<norm_end:
        # The generated law projection stays in the scene; the figures act.
        if t<statement+min(2.9,.55*(norm_end-statement)):
            im=edit(A['05-law1'],A['04-zylla-glance'],M['zylla_head'],
                    window(t,14.27,14.40,15.26,15.43))
            im=edit(im,A['02-brakk-tense'],M['brakk_expression'],
                    window(t,15.51,15.62,15.94,16.06))
            return im
        im=Image.blend(A['04-statement'],A['04-zylla-glance'],
                       max(window(t,17.20,17.33,17.70,17.85),
                           window(t,18.41,18.53,18.90,19.07)))
        return cut(im,1.16,(680,770))
    if t<consent_end:
        if t<norm_end+min(2.0,.49*(consent_end-norm_end)):
            return edit(A['06-law2'],A['04-zylla-glance'],M['zylla_head'],
                        window(t,19.92,20.05,20.59,20.77))
        return A['07-shield']
    x=T['cross_at']
    if t<x:
        im=A['07-shield']
        # The shield lands with a brief light pulse, without camera shaking.
        if T['shield_at']<t<T['shield_at']+.19:
            im=ImageEnhance.Brightness(im).enhance(1.055)
        return im
    v=min(1,max(0,(t-x)/.16))
    im=edit(A['07-shield'],A['08-cross'],M['paper'],v)
    # Last reaction: the raised hand relaxes and Brakk understands the result.
    if t>26.00:
        im=Image.blend(A['08-cross'],A['08-brakk-deflated'],
                       min(1,(t-26.00)/.18))
    if t>26.99:return cut(im,1.14,(585,1025))
    return im

def main():
    p=argparse.ArgumentParser();p.add_argument('--timing',required=True);p.add_argument('--out',required=True)
    args=p.parse_args();T=json.loads(Path(args.timing).read_text())
    names=['01-consent','01-reject','02-interrogation','02-later-tired',
           '02-brakk-tense','03-slam','04-statement','04-zylla-glance',
           '05-law1','06-law2','07-shield','08-cross','08-brakk-deflated']
    A={n:source(n) for n in names}
    M={'scanner':soft_rect((698,615,940,960),18),
       'brakk_face':soft_ellipse((555,115,830,540),14),
       'brakk_expression':soft_ellipse((295,296,482,508),7),
       'clock':soft_ellipse((480,140,670,345),8),
       'zylla_face':soft_ellipse((590,470,925,905),14),
       'zylla_eyes':soft_ellipse((628,735,839,841),6),
       'zylla_head':soft_ellipse((560,485,930,920),12),
       'paper':soft_rect((290,875,830,1290),12)}
    dest=Path(args.out);dest.parent.mkdir(parents=True,exist_ok=True)
    n=math.ceil(T['final_duration']*FPS)
    cmd=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pixel_format','rgb24',
         '-video_size',f'{W}x{H}','-framerate',str(FPS),'-i','pipe:0',
         '-vf','scale=1080:1920:flags=lanczos,format=yuv420p','-c:v','libx264',
         '-preset','veryfast','-crf','19','-pix_fmt','yuv420p',str(dest)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for k in range(n):proc.stdin.write(render_frame(k/FPS,T,A,M).tobytes())
        proc.stdin.close()
        if proc.wait():raise RuntimeError('Video-Encoder fehlgeschlagen')
    except BaseException:
        proc.kill();raise
    print(f'{dest}: {n} frames, {n/FPS:.2f}s, 30 fps')

if __name__=='__main__':main()
