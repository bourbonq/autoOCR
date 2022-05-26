import numpy as np
import os
from random import randint, choice, sample

character_path = "../source/chinese_character.txt"
paragraph_path = "../source/paragraph"
font_path = "../source/fonts"

def pos_division():
    #x1, y1 = randint(0, 1600), randint(0, 900)
    y_lib = [0, 200, 400, 600, 800]
    rec = []
    for i in range(len(y_lib)):
        a = [num for num in range(1920)]
        x_lib = sample(a, randint(3, 10))
        x_lib = sorted(x_lib, reverse=False)
        for j in range(len(x_lib)):
            if j == len(x_lib) - 1:
                rec.append([x_lib[j], y_lib[i], 1920, y_lib[i] + 200])
            else:
                rec.append([x_lib[j], y_lib[i], x_lib[j + 1], y_lib[i] + 200])
    return rec

def choose_rec(rec):
    tar = choice(rec)
    x1, y1, x2, y2 = tar
    rec.remove(tar)
    return x1, y1, x2, y2, rec

def random_generation():
    word_list = []
    num = randint(1, 10)
    print("num of random word: %d" %num)
    #choose word type
    word_type = int(input("please input word type:\n1: random chinese_character\n2: paragraph\n"))
    if word_type == 1:
        word_path = character_path
        with open(word_path, 'r') as f:
            word_line = f.readlines()
            word_lib = word_line[0].strip()
    elif word_type == 2:
        word_path = paragraph_path + "/" + choice(os.listdir(paragraph_path))
        with open(word_path, 'r') as f:
            word_line = f.readlines()
            word_lib = [x.strip() for x in word_line]
    #divide background into random rectangles
    rec = pos_division()
    for w_id in range(num):
        ran = randint(1, 10)
        if word_type == 1:
            #random chinese character combination
            label = ''.join(sample(word_lib, ran))
        elif word_type == 2:
            #choose a random line and get random word
            line = choice(word_lib)
            if len(line) <= ran:
                label = line
            else:
                start = randint(0, len(line) - ran)
                label = line[start : start + ran]
        size = randint(20, 200)
        '''
        x1, y1 = randint(0, 1600), randint(0, 900)
        x2, y2 = randint(x1 + 1, 1920), randint(y1 + 1, 1080)
        '''
        #choose a rectangle as the range of position
        x1, y1, x2, y2, rec = choose_rec(rec)
        family = choice(os.listdir(font_path))
        b, g, r = randint(0, 255), randint(0, 255), randint(0, 255)
        #extra infomation for future use
        style = "111"
        weight = "222"

        word_list.append({'id':w_id, 'label':label, 'size':size, 'position':{'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2}, 'family':family, 'color':{'b':b, 'g':g, 'r':r}, 'style':style, 'weight':weight})

    return word_list

def manual_generation():
    word_list = []
    num = int(input("please input num of words(num >= 1):\n"))
    font_list = os.listdir(font_path)
    font_str = ""
    for i in range(len(font_list)):
        font_str += (str(i + 1) + ":" + font_list[i] + "\n")
    for w_id in range(num):
        label = input("please input label of word %d:\n" %w_id)
        size = int(input("please input size of word %d:\n" %w_id))
        position = input("please input position of word %d(x1,y1,x2,y2 separated by space):\n" %w_id)
        fid = int(input("please input font family id of word %d:\n%s" %(w_id, font_str)))
        color = input("please input color of word %d(b,g,r separated by space):\n" %w_id)
        style = input("please input style of word %d:\n" %w_id)
        weight = input("please input weight of word %d:\n" %w_id)
        
        family = font_list[fid - 1]
        x1, y1, x2, y2 = [int(val) for val in position.split()]
        b, g, r = [int(val) for val in color.split()]

        word_list.append({'id':w_id, 'label':label, 'size':size, 'position':{'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2}, 'family':family, 'color':{'b':b, 'g':g, 'r':r}, 'style':style, 'weight':weight})

    return word_list

def gen_yaml_doc(yaml_path, word_list):
    from ruamel import yaml
    file = open(yaml_path, 'w', encoding='UTF-8')
    yaml.dump(word_list, file, Dumper=yaml.RoundTripDumper, allow_unicode=True)
    file.close()

word_list = []
#choose generate method
gen_method = int(input("please input generation method:\n1: manual generation\n2: random generation\n"))
if gen_method == 1:
    word_list = manual_generation()
elif gen_method == 2:
    word_list = random_generation()

#record word_list in input/word.yaml
yaml_path = "../input/word.yaml"
gen_yaml_doc(yaml_path, word_list)
print("generate words succesfully!")
