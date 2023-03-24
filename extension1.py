'''Author: Eric Adjei Appiah
CS 151 Section: B
Fall 2022
Date: 10th November, 2022
'''


from lab07 import *
import turtle as trt


def main():
    '''Converts message input by a user into a drawn braille'''
    message = input("What message do you wish to translate?\n")
    bs=translator(message,braille_dictionary)
    draw_word(trt, bs)
    draw_braille_character(trt, bs)
