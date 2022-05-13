import numpy as np
import os
from random import randint, choice

string_dic = ["aaa", "b", "xxx"]
family_dic = ["sonti", "kaiti", "heiti"]

def random_generation():
    word_list = []
    num = randint(1, 10)
    print("num of word: %d" %num)
    for w_id in range(num):
        label = choice(string_dic)
        size = randint(1, 20)
        x1, y1, x2, y2 = randint(0, 1920), randint(0, 1080), randint(0, 1920), randint(0, 1080)
        family = choice(family_dic)
        b, g, r = randint(0, 255), randint(0, 255), randint(0, 255)
        style = "111"
        weight = "222"

        word_list.append({'id':w_id, 'label':label, 'size':size, 'position':{'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2}, 'family':family, 'color':{'b':b, 'g':g, 'r':r}, 'style':style, 'weight':weight})

    return word_list

def manual_generation():
    word_list = []
    num = int(input("please input num of word(num >= 1):\n"))
    for w_id in range(num):
        label = input("please input label of word %d:\n" %w_id)
        size = int(input("please input size of word %d:\n" %w_id))
        position = input("please input position of word %d(x1,y1,x2,y2 separated by space):\n" %w_id)
        family = input("please input font family of word %d:\n" %w_id)
        color = input("please input color of word %d(b,g,r separated by space):\n" %w_id)
        style = input("please input style of word %d:\n" %w_id)
        weight = input("please input weight of word %d:\n" %w_id)

        x1, y1, x2, y2 = [int(val) for val in position.split()]
        b, g, r = [int(val) for val in color.split()]

        word_list.append({'id':w_id, 'label':label, 'size':size, 'position':{'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2}, 'family':family, 'color':{'b':b, 'g':g, 'r':r}, 'style':style, 'weight':weight})

    return word_list

def gen_yaml_doc(yaml_path, word_list):
    from ruamel import yaml
    file = open(yaml_path, 'w', encoding='utf-8')
    yaml.dump(word_list, file, Dumper=yaml.RoundTripDumper)
    file.close()

word_list = []
gen_method = int(input("please input generation method:\n1: manual generation\n2: random generation\n"))
if gen_method == 1:
    word_list = manual_generation()
elif gen_method == 2:
    word_list = random_generation()

#print(word_list)

yaml_path = "../input/word2.yaml"
gen_yaml_doc(yaml_path, word_list)
