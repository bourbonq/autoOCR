import numpy as np
import os
from read_yaml import *
from random import randint
from PIL import Image, ImageFont, ImageDraw

font_lib_path = "/home/qh/Fonts"
word_path = "../input/word2.yaml"
pic_path = "../input/pic.yaml"

def gen_image(pic_info):
    pic_height = pic_info['size']['height']
    pic_width = pic_info['size']['width']
    pic_b = pic_info['color']['b']
    pic_g = pic_info['color']['g']
    pic_r = pic_info['color']['r']

    img = Image.new("RGB", (pic_height, pic_width), (pic_r, pic_g, pic_b))

    return img

def draw_text(img, word):
    draw = ImageDraw.Draw(img)
    wid = word['id']
    label = word['label']
    size = word['size']
    family = word['family']
    x1 = word['position']['x1']
    y1 = word['position']['y1']
    x2 = word['position']['x2']
    y2 = word['position']['y2']
    r = word['color']['r']
    g = word['color']['g']
    b = word['color']['b']

    font_path = os.path.join(font_lib_path, family)
    if os.path.exists(font_path):
        font = ImageFont.truetype(font_path, size=size, encoding="utf-8")
    else:
        raise Exception(family + " not exist!")

    w, h = draw.textsize(label, font=font)
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1
    print(x)
    print(y)
    draw.text((x, y), label, align='center', font=font, fill=(r, g, b))

    draw.rectangle([x1, y1, x2, y2])

    return img

word_info = read_yaml_ruamel(word_path)
pic_info = read_yaml_ruamel(pic_path)
#print(word_info)
#print(pic_info)

img = gen_image(pic_info)

for word in word_info:
    img = draw_text(img, word)

img.show()

