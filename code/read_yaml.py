import os
import yaml

def read_yaml_all(path):
    with open(path, 'r') as f:
        temp = yaml.load_all(f.read(), Loader = yaml.FullLoader)
    for i in temp:
        print(i)
    return temp
