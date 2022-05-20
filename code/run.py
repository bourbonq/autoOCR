import numpy as np
import os
from read_yaml import *
import random
from PIL import Image, ImageFont, ImageDraw

font_lib_path = "../source/fonts"
word_path = "../input/word0.yaml"
pic_path = "../input/pic.yaml"
yaml_path = "../output/mark.yaml"
pro_font = ['msyh.ttc', 'FZYTK.TTF', 'STFANGSO.TTF', 'STKAITI.TTF', 'STSONG.TTF', 'STZHONGS.TTF', 'STXIHEI.TTF']
out_path = "../output/res.png"

def gen_image(pic_info):
    pic_height = pic_info['size']['height']
    pic_width = pic_info['size']['width']
    pic_b = pic_info['color']['b']
    pic_g = pic_info['color']['g']
    pic_r = pic_info['color']['r']

    img = Image.new("RGB", (pic_width, pic_height), (pic_r, pic_g, pic_b))

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
    x_min = int((x2 - x1) / len(label))
    y_min = y2 - y1
    #print("size:%d\nx_min:%d\ny_min:%d" %(size, x_min, y_min))
    if size < x_min and size < y_min:
        x2 = x1 + size * len(label)
        y2 = y1 + size
    elif x_min < size and x_min < y_min:
        size = x_min
        y2 = y1 +size
    else:
        size = y_min
        x2 = x1 + size * len(label)
    #print("size:%d\nx2:%d\ny2:%d" %(size, x2, y2))

    font_path = os.path.join(font_lib_path, family)
    if os.path.exists(font_path):
        font = ImageFont.truetype(font_path, size=size, encoding="utf-8")
    else:
        raise Exception(family + " not exist!")

    #w, h = draw.textsize(label, font=font)
    #x = (x2 - x1 - w)/2 + x1
    #y = (y2 - y1 - h)/2 + y1
    x = x1
    y = y1

    draw.text((x, y), label, align='left', font=font, fill=(r, g, b))
    
    if family in pro_font:
        offset = int(0.15 * size)
        y1 += offset
        y2 += offset

    #draw.rectangle([x1, y1, x2, y2])

    mark = {'id':wid, 'bbox':[x1, y1, x2, y2], 'label':label, 'keyword':'keyword'}
    return img, mark

def gen_yaml_doc(yaml_path, mark_list):
    from ruamel import yaml
    file = open(yaml_path, 'w', encoding='UTF-8')
    yaml.dump(mark_list, file, Dumper=yaml.RoundTripDumper, allow_unicode=True)
    file.close()

word_info = read_yaml_ruamel(word_path)
#print(word_info)

mode = int(input("please input mode of background:\n1:specified monochrome\n2:random picture\n"))
if mode == 1:
    pic_info = read_yaml_ruamel(pic_path)
    img = gen_image(pic_info)
elif mode == 2:
    random.seed()
    src_img_path = "../source/picture/" + random.choice(os.listdir("../source/picture"))
    img = Image.open(src_img_path).resize((1920, 1080))

mark_list = []
for word in word_info:
    img, mark = draw_text(img, word)
    mark_list.append(mark)

gen_yaml_doc(yaml_path, mark_list)
img.save(out_path)
img.show()

