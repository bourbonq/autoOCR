autoOCR
===========================

#Introduction

This tool is usd to paint Chinese characters on the picture automatically. You can specify the way to generate target images.

#Enviroment dependency

Python 3.7.5+
Pillow 5.4.1+

#How to use autoOCR

1. Run "python3 gen_character.py" if chinese_character.txt does not exist in source directory.

2. Run "python3 gen_word.py" to generate words with parameters in input/word.yaml.

   generation method:
   1. manual generation: manually input all word information.
   2. random generation: random generate word information.

   word type:
   1. random chinese_character: choose random Chinese characters from chinese_character.txt.
   2. paragraph: choose random pieces from sentences in a txt file in paragraph directory.

3. Run "python3 gen_word.py" to paint words on a picture by pillow.

   mode of background:
   1. specified monochrome: before running run.py, please  specify picture information in input/pic.yaml.
   2. random monochrome: random choose a color as the background. 
   3. random picture: choose a picture as the background of the final image from source directory.

   The final image is stored in output/res.png and the mark file is stored in output/mark.yaml.

#Directory structure description

autoOCR
├── Readme.md                   // help
├── code                        
│   ├── gen_character.py	// generate chinese_character.txt
│   ├── gen_word.py             // generate words with parameters
│   ├── read_yaml.py            // read yaml files
│   ├── run_cv.py               // paint words by opencv, no use at present
│   └── run.py                  // paint words on a picture by pillow
├── input
│   ├── pic.yaml                // picture configuration if mode is monochrome
│   └── word.yaml               // word configuration
├── output                      // generate res.png and mark.yaml after running run.cv
├── requirements.txt            // enviroment requirements
└── source                      // source for words, pictures, etc.
    ├── chinese_character.txt   // a Chinese character library
    ├── fonts                   // available font family for Chinese characters
    ├── paragraph               // paragraphs for obtain Chinese characters
    └── picture                 // pictures as the background of the final image

#Additional instructions

Future work:
1. Write scripts in order to specify the location and form of input and output.
2. Some fonts can not be adapted to complex Chinese characters.

The autoOCR Developers
