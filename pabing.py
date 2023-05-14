def watermark():
    im = Image.open("1080p.jpg")
    font = ImageFont.truetype(font='字魂59号-创粗黑.ttf', size=30)
    draw = ImageDraw.Draw(im)
    textv = text()
    draw.text(xy=(80,50),text=textv,fill=(255,255,255),font=font)
    im.save("加水印.jpg")
def text():
    import requests
    url = "https://cn.bing.com/HPImageArchive.aspx?n=1&format=js&idx=0"
    res = requests.get(url)
    res.encoding = "UTF-8"
    a = res.text
    b = a.split(",")
    text = b[5]
    text = text.split(":")
    text = text[1]
    text = text[1:-1]
    print(text)
    return(text)
def paimg(c):
    if c == "d":
        d = "_1920x1080.jpg"
        g = "1080p.jpg"
    else:
        d = "_800x480.jpg"
        g = "480p.jpg"
    import requests
    url = "https://cn.bing.com/HPImageArchive.aspx?n=1&format=js&idx=0"
    res = requests.get(url)
    res.encoding = "UTF-8"
    a = res.text
    b = a.split(",")
    web = b[4]
    web = web.split(":")
    web = web[1]
    web = web[1:-1]
    print(web)
    f = "https://s.cn.bing.net"
    newweb = f + web + d
    print(newweb)
    res = requests.get(newweb)
    pic = res.content
    with open(g,"wb") as file:
       file.write(pic)
import easygui as g
import sys
import PIL
from PIL import Image,ImageDraw,ImageFont
if g.ccbox("欢迎使用bing壁纸",choices=("使用","退出")):
    paimg("c")
    if g.ccbox(text(),image = "480p.jpg",choices=("点我退出(480p壁纸已保存至源码文件夹下)","下载1080p")):
        sys.exit(0)
    else:
        paimg("d")
        textvi = "是否要添加水印\n" + text()
        if g.ccbox(textvi,choices=("要","不要（退出）")):
            watermark()
            g.msgbox("已添加水印")
        else:
            sys.exit(0)
else:
    sys.exit(0)
