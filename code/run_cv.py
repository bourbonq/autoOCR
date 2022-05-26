#use opencv to realize some function, but not used at present
import numpy as np
import cv2 as cv
from read_yaml import *
from random import randint
from PIL import Image, ImageFont, ImageDraw

word_path = "../input/word.yaml"
pic_path = "../input/pic.yaml"i
'''
word_info = read_yaml_all(word_path)
pic_info = read_yaml_single(pic_path)
'''
pic_height = pic_info['size']['height']
pic_width = pic_info['size']['width']
pic_b = pic_info['color']['b']
pic_g = pic_info['color']['g']
pic_r = pic_info['color']['r']

pic = np.zeros((pic_height, pic_width, 3), dtype=np.uint8)
pic[:,:,0] = pic_b
pic[:,:,1] = pic_g
pic[:,:,2] = pic_r

s = None
font = cv.FONT_HERSHEY_SIMPLEX
while s != "#":    
    s = input("Please input string:")
    if s == "#":
        break
    if not s:
        raise Exception("string can't be null!")
    cv.putText(pic, s, (randint(0, 1000), randint(-5, 600)), font, 3, (0, 255, 0), randint(5, 15))

cv.putText(pic, s, (900, 0), font, 3, (0, 255, 0), 15)
'''
a = cv.imread("../pic/3f006fb4c4ff4249826e34b55040f2bc.jpg", -1)
'''
cv.namedWindow("pic")
cv.imshow("pic", pic)

key = cv.waitKey()
if key != -1:
    cv.destroyAllWindows()

