import numpy as np
import cv2 as cv
from read_yaml import read_yaml_all

s = None
arr = []
word_path = "../input/word.yaml"
pic_path = "../input/pic.yaml"
word_lib = read_yaml_all(word_path)
pic_lib = read_yaml_all(pic_path)

'''
while (s = input("Please input string:")) != "#":
    arr.append(s)

a = cv.imread("../pic/3f006fb4c4ff4249826e34b55040f2bc.jpg", -1)
cv.namedWindow("pic")
cv.imshow("pic", a)
print(a)
key = cv.waitKey()
if key != -1:
    cv.destroyAllWindows()
'''
