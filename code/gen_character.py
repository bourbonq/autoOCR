import codecs

#used to generate chinense character library in source/chinese_character.txt
char_path = "../source/chinese_character.txt"
start, end = (0x4e00, 0x9fa5)
with codecs.open(char_path, 'wb', encoding="utf-8") as f:
    for codepoint in range(int(start), int(end)):
        f.write(unichr(codepoint))
