import os
'''
def read_yaml_all(path):
    import yaml
    lib = []
    with open(path, 'r') as f:
        temp = yaml.load_all(f.read(), Loader=yaml.FullLoader)
    for i in temp:
        #print(i)
        lib.append(i)
    return lib

def read_yaml_single(path):
    import yaml
    with open(path, 'r') as f:
        temp = yaml.load(f.read(), Loader=yaml.FullLoader)
    #print(temp)
    return temp
'''
def read_yaml_ruamel(path):
    from ruamel import yaml
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file.read(), Loader=yaml.Loader)
    file.close()
    return data
