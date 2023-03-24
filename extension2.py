'''Author: Eric Adjei Appiah
CS 151 Section: B
Fall 2022
Date: 10th November, 2022
'''

from lab07 import *
import turtle as trt

def main():
    '''Reads the alice text file and converts it into a drawn braille'''
    file = open('alice.txt','r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        bs=translator(line,braille_dictionary)
        draw_word(trt, bs)
    file.close()
main()
