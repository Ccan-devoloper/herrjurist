#!/usr/bin/env python3
"""Render a small number of locked, full-resolution shots as limited animation.

Every moving element comes from a tightly edited variant of the SAME master.
There is no generic per-frame zoom and no replacement of the whole drawing for
blink, mouth, clock or fist motion.
"""
import argparse
import json
import math
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance

ROOT = Path(__file__).resolve().parent
W, H, FPS = 940, 1672, 30
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def source(name):
    im = Image.open(ROOT / 'masters' / name).convert('RGB')
    return im.resize((W,H), Image.Resampling.LANCZOS) if im.size != (W,H) else im

def feather_ellipse(box, radius=12):
    m=Image.new('L',(W,H)); d=ImageDraw.Draw(m); d.ellipse(box,fill=255)
    return m.filter(ImageFilter.GaussianBlur(radius))

def feather_rect(box, radius=12):
    m=Image.new('L',(W,H)); d=ImageDraw.Draw(m); d.rectangle(box,fill=255)
    return m.filter(ImageFilter.GaussianBlur(radius))

def local_edit(base, edited, mask, amount):
    if amount<=0: return base.copy()
    factor=mask.point(lambda x: int(x*min(1,amount)))
    return Image.composite(edited,base,factor)

def homography(source_size, quad):
    sw,sh=source_size
    uv=[(0,0),(sw,0),(sw,sh),(0,sh)]
    A=[]; b=[]
    for (x,y),(u,v) in zip(quad,uv):
        A.append([x,y,1,0,0,0,-u*x,-u*y]);b.append(u)
        A.append([0,0,0,x,y,1,-v*x,-v*y]);b.append(v)
    return np.linalg.solve(np.array(A,float),np.array(b,float))

def paper_ink(im, final=False, signature=0):
    # Draw the legal meaning on the physical sheet before the scene is filmed.
    tile=Image.new('RGBA',(480,240),(0,0,0,0));d=ImageDraw.Draw(tile)
    d.text((20,12),'EINWILLIGUNG',font=ImageFont.truetype(FONT,42),fill=(48,39,36,225))
    d.text((21,80),'Aussage verwerten',font=ImageFont.truetype(FONT,28),fill=(66,50,41,210))
    d.line([(20,137),(440,137)],fill=(85,64,50,130),width=3)
    if final:
        quad=[(34,950),(226,915),(448,1080),(105,1150)]
    else:
        quad=[(448,887),(790,925),(663,1085),(327,1035)]
    warp=tile.transform((W,H),Image.Transform.PERSPECTIVE,homography(tile.size,quad),Image.Resampling.BICUBIC)
    out=im.convert('RGBA');out.alpha_composite(warp)
    if signature and not final:
        # Ink appears next to the pen rather than teleporting in one frame.
        d=ImageDraw.Draw(out)
        pts=[(470,1132),(489,1123),(500,1141),(514,1119),(523,1139),(541,1131)]
        total=max(1,min(len(pts),int(signature*(len(pts)+1))))
        if total>1:d.line(pts[:total],fill=(28,24,27,220),width=3,joint='curve')
    return out.convert('RGB')

def close_cut(im, scale, center):
    if scale==1:return im
    cw,ch=int(W/scale),int(H/scale)
    cx,cy=center
    x=max(0,min(W-cw,int(cx-cw/2))); y=max(0,min(H-ch,int(cy-ch/2)))
    return im.crop((x,y,x+cw,y+ch)).resize((W,H),Image.Resampling.LANCZOS)

def caption_board(im, phase, show_sub=True):
    out=im.convert('RGBA'); layer=Image.new('RGBA',(W,H));d=ImageDraw.Draw(layer)
    main=ImageFont.truetype(FONT,83);small=ImageFont.truetype(FONT,55)
    # Appear one line at a time on the front-on plane of the drawn hologram.
    title='§ 136a StPO' if phase=='norm' else 'Abs. 3 StPO'
    sub='ERMÜDUNG' if phase=='norm' else 'EINWILLIGUNG'
    items=[(title,268,main,(255,225,181,255))]
    if show_sub:items.append((sub,405,small,(255,157,62,255)))
    for txt,y,font,col in items:
        bb=d.textbbox((0,0),txt,font=font); x=(W-(bb[2]-bb[0]))//2
        d.text((x,y),txt,font=font,fill=col,stroke_width=2,stroke_fill=(88,35,4,240))
    glow=layer.filter(ImageFilter.GaussianBlur(9));glow.putalpha(glow.getchannel('A').point(lambda v:int(v*.30)))
    out.alpha_composite(glow);out.alpha_composite(layer)
    return out.convert('RGB')

def recorder_on(im, amp):
    overlay=Image.new('RGBA',(W,H));d=ImageDraw.Draw(overlay)
    d.ellipse((279,1115,298,1134),fill=(255,72,35,int(230*amp)))
    for i in range(7):
        x=305+i*15; hh=(7+(i*19)%24)*amp
        d.line((x,1124-hh,x,1124+hh),fill=(255,149,41,int(220*amp)),width=3)
    out=im.convert('RGBA');out.alpha_composite(overlay)
    return out.convert('RGB')

def warm_pulse(im, t, strength=.02):
    v=strength*(.5+.5*math.sin(2*math.pi*1.2*t))
    return ImageEnhance.Brightness(im).enhance(1+v)

def frame(t,b,assets,masks):
    # The narration boundaries dictate editorial beats; holds are deliberately
    # uneven. A major gesture is an 8-cel burst, followed by a stable hold.
    scene=max(0,min(len(b)-2,next((i for i in range(len(b)-1) if b[i]<=t<b[i+1]),len(b)-2)))
    start,end=b[scene],b[scene+1];u=(t-start)/(end-start)
    if scene==0:
        im=paper_ink(assets['consent'],signature=min(1,u*3))
        if u>.48:
            q=min(1,(u-.48)/.12)
            lit=paper_ink(assets['reject'],signature=min(1,u*3))
            im=local_edit(im,lit,masks['scanner'],q)
            if u>.63:im=close_cut(im,1.18,(732,945))  # a deliberate cut
        return warm_pulse(im,t,.012)
    if scene==1:
        im=assets['wide']
        if u<.32: im=close_cut(im,1.65,(598,265))  # clock is a distinct insert
        return warm_pulse(im,t,.018)
    if scene==2:
        if u<.50:
            clock_amt=min(1,max(0,(u-.13)/.14))
            im=local_edit(assets['wide'],assets['later'],masks['clock'],clock_amt)
            return warm_pulse(im,t,.05)
        if u<.80:
            v=(u-.50)/.30
            a=min(1,max(0,(v-.32)/.25))
            im=local_edit(assets['close'],assets['blink'],masks['eyes'],a)
            return warm_pulse(im,t,.016)
        v=(u-.80)/.20
        im=local_edit(assets['wide'],assets['fist'],masks['fist'],min(1,v*3))
        return im
    if scene==3:
        if u<.13:
            v=min(1,u/.13)
            im=local_edit(assets['fist'],assets['wide'],masks['fist'],v)
            if .04<u<.11:im=ImageEnhance.Brightness(im).enhance(1.10)
            return close_cut(im,1.08,(190,900))
        if u<.32:
            v=min(1,(u-.13)/.12)
            return local_edit(assets['close'],assets['startle'],masks['face'],v)
        # Tiny mouth alternation: the body and set stay pixel-identical.
        v=(u-.32)/.68
        mouth=max(0,math.sin(2*math.pi*2.1*v))*.85
        im=local_edit(assets['close'],assets['speaking'],masks['mouth'],mouth)
        return recorder_on(im,min(1,v*3))
    if scene==4:
        im=assets['board']
        if u>.16:im=caption_board(im,'norm',show_sub=u>.45)
        if u>.57:im=close_cut(im,1.22,(470,360))
        return warm_pulse(im,t,.03)
    if scene==5:
        if u<.29:
            return caption_board(assets['board'],'consent')
        v=(u-.29)/.71
        before=assets['pre']
        if v<.28:return paper_ink(before,final=True)
        effect=min(1,(v-.28)/.12)
        im=local_edit(before,assets['impact'],masks['shield'],effect)
        if .28<v<.43:im=ImageEnhance.Brightness(im).enhance(1+.13*math.sin(math.pi*effect))
        return paper_ink(im,final=True)
    im=paper_ink(assets['impact'],final=True)
    if u>.35:
        crossed=paper_ink(assets['cross'],final=True)
        im=local_edit(im,crossed,masks['paper'],min(1,(u-.35)/.15))
    return im

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--timing',default=str(ROOT/'out/timing.json'))
    ap.add_argument('--out',default=str(ROOT/'out/silent.mp4'));ap.add_argument('--preview',action='store_true')
    args=ap.parse_args()
    if args.preview:
        b=[0,4.2,7.7,12.2,16.6,22.2,27.2,30.0]
    else:
        b=json.loads(Path(args.timing).read_text())['boundaries']
    a={
        'consent':source('01-consent.jpg'),'reject':source('01-scanner-reject.jpg'),
        'wide':source('02-interrogation.jpg'),
        'later':source('02-later-clock.jpg'),'fist':source('02-fist-raised.jpg'),
        'close':source('03-zylla-exhausted.jpg'),'blink':source('03-zylla-blink.jpg'),
        'startle':source('03-zylla-startled.jpg'),'speaking':source('03-zylla-speaking.jpg'),
        'board':source('04-law-board.jpg'),'pre':source('05-before-shield.jpg'),
        'impact':source('05-shield-impact.jpg'),'cross':source('05-crossed-paper.jpg')}
    masks={
        'scanner':feather_rect((675,550,939,1050),25),
        'clock':feather_ellipse((454,97,779,428),10),
        'fist':feather_rect((0,525,355,1013),23),
        'eyes':feather_ellipse((302,350,690,718),28),
        'face':feather_ellipse((294,332,694,770),24),
        'mouth':feather_ellipse((386,531,587,757),22),
        'shield':feather_rect((420,260,890,1005),35),
        'paper':feather_rect((0,860,660,1250),15)}
    dest=Path(args.out);dest.parent.mkdir(parents=True,exist_ok=True)
    n=math.ceil(b[-1]*FPS)
    cmd=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pixel_format','rgb24',
         '-video_size',f'{W}x{H}','-framerate',str(FPS),'-i','pipe:0',
         '-vf','scale=1080:1920:flags=lanczos,format=yuv420p',
         '-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p',str(dest)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for k in range(n):proc.stdin.write(frame(k/FPS,b,a,masks).tobytes())
        proc.stdin.close()
        code=proc.wait()
        if code:raise RuntimeError(f'ffmpeg returned {code}')
    except BaseException:
        proc.kill();raise
    print(f'{dest} · {n} frames · {n/FPS:.2f}s · 30 fps')

if __name__=='__main__':main()
