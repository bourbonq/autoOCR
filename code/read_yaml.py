import os

#used to read yaml file according to file path
def read_yaml_ruamel(path):
    from ruamel import yaml
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file.read(), Loader=yaml.Loader)
    file.close()
    return data
