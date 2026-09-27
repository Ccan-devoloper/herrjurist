#!/usr/bin/env python3
"""30 fps video from stable cartoon cels. No compositor type or camera jitter."""
import argparse
import json
import math
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

ROOT=Path(__file__).resolve().parent
W,H,FPS=941,1672,30

def source(name):
    return Image.open(ROOT/'masters'/f'{name}.jpg').convert('RGB')

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
        return im
    if t<sleepy:
        im=A['02-interrogation']
        clock=min(1,max(0,(t-interrogation-.12)/.25))
        im=edit(im,A['02-later-tired'],M['clock'],clock)
        blink=min(1,max(0,(t-interrogation-.62)/.20))
        im=edit(im,A['02-later-tired'],M['zylla_face'],blink)
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
        if t>statement-.72:return cut(A['04-statement'],1.43,(175,1255))
        return A['04-statement']
    if t<norm_end:
        # One short in-world legal hologram, then the character gets the frame.
        if t<statement+min(2.9,.55*(norm_end-statement)):
            return A['05-law1']
        return cut(A['04-statement'],1.16,(680,770))
    if t<consent_end:
        if t<norm_end+min(2.0,.49*(consent_end-norm_end)):
            return A['06-law2']
        return A['07-shield']
    x=T['cross_at']
    if t<x:return A['07-shield']
    v=min(1,max(0,(t-x)/.16))
    im=edit(A['07-shield'],A['08-cross'],M['paper'],v)
    if t>x+.45:return cut(im,1.14,(585,1025))
    return im

def main():
    p=argparse.ArgumentParser();p.add_argument('--timing',required=True);p.add_argument('--out',required=True)
    args=p.parse_args();T=json.loads(Path(args.timing).read_text())
    names=['01-consent','01-reject','02-interrogation','02-later-tired','03-slam','04-statement','05-law1','06-law2','07-shield','08-cross']
    A={n:source(n) for n in names}
    M={'scanner':soft_rect((698,615,940,960),18),
       'brakk_face':soft_ellipse((555,115,830,540),14),
       'clock':soft_ellipse((480,140,670,345),8),
       'zylla_face':soft_ellipse((590,470,925,905),14),
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
