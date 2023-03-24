'''Author: Eric Adjei Appiah
CS 151 Section: B
Fall 2022
Date: 10th November, 2022
'''


# import your file name (whatever it is)
from lab07 import *

import json
import time
import turtle
import urllib.request

# Global variables that store the location of files.
# Change these to match the relative addresses of the files on your computer
TEST_WORD_FILENAME = "hw4TextFiles/test-words.txt"



# ========================================================================
# Test for Question 1 - Braille (Part 1)

def test_braille_dictionary():
    """Tests the braille_dictionary contents."""

    print()
    print("-------------------------------------")
    print("Testing braille_dictionary contents:")
    print("key\tvalue")

    for key in braille_dictionary:
        print(key, "\t", braille_dictionary[key])


# ========================================================================
# Test for Question 2 - Braille (Part 2)

def test_translator():
    """Tests the translator function. Note that details about specific test calls are
    printed if the function FAILS the test."""
    
    print()
    print("-------------------------------------")
    print("Testing translator():")


    s1 = "the quick brown fox jumps over the lazy dog"
    print(s1)
    print(translator(s1, braille_dictionary))
    print()
    assert translator(s1, braille_dictionary) == [[[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]], [[1, 1, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1], \
        [0, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0]], [[1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1], \
        [1, 0, 1, 1, 1, 0]], [[1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 1]], [[0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 0, 0], 
        [1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0]], [[0, 1, 1, 1, 1, 0], 
        [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]], [[1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1]], [[1, 0, 0, 1, 1, 0], \
        [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0]]] 

    s2 = "do it as you will"
    print(s2)
    print(translator(s2, braille_dictionary))
    print()
    assert translator(s2, braille_dictionary) == [[1, 0, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1]]

    s3 = "from every corner of the planet, people go and seek more knowledge"
    print(s3)
    print(translator(s3, braille_dictionary))
    print()
    assert translator(s3, braille_dictionary) == [[1, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [[1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 1, 1, 0, 1, 0], 
        [1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0]], [[1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0]], [[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], 
        [1, 0, 0, 0, 1, 0]], [[1, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0]], 
        [1, 1, 1, 1, 0, 0], [1, 1, 0, 1, 1, 0], [[1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0]], [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], 
        [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0]], [1, 0, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0]]

    s4 = "It's possible we can do more with just very little."
    print(s4)
    print(translator(s4, braille_dictionary))
    print()
    assert translator(s4, braille_dictionary)== [[[0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0], 
        [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]], [[0, 1, 0, 1, 1, 1], 
        [1, 0, 0, 0, 1, 0]], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 1, 1, 0, 0], [[0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], 
        [1, 1, 0, 0, 1, 0]], [0, 1, 0, 1, 1, 0], [1, 1, 1, 0, 0, 1], [[1, 1, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]]]

    s5 = "I have quite the conundrum that may come back to bite us."
    print(s5)
    print(translator(s5, braille_dictionary))
    print()
    assert translator(s5, braille_dictionary) ==  [[0, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 0], [[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0]], [[1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0], 
        [1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 0, 0]], [0, 1, 1, 1, 1, 0], [[1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1]],
        [[1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0]], [[1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], 
        [1, 0, 1, 0, 0, 0]], [[0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0]], [[1, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0]], 
        [[1, 0, 1, 0, 0, 1], [0, 1, 1, 1, 0, 0]]]
    
    
    s6 = "We have to do this so that racoons don't come back again."
    print(s6)
    print(translator(s6, braille_dictionary))
    print()
    assert translator(s6, braille_dictionary) == [[[0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0]], [1, 1, 0, 0, 1, 0], [[0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0]],
        [1, 0, 0, 1, 1, 0], [[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0]], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0],
        [[1, 1, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0]], 
        [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0]], [[1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0], 
        [1, 0, 0, 0, 1, 0]], [[1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0]], [[1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0], 
        [1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 1, 1, 1, 0]]]

    s7 = "But rather then start over, why not be more like her and never give up?"
    print(s7)
    print(translator(s7, braille_dictionary))
    print()
    assert translator(s7, braille_dictionary) == [[1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0], [[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 0]], [[0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0]], [[1, 0, 1, 0, 1, 0], 
        [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0]], [[0, 1, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 1]], [1, 0, 1, 1, 1, 0], 
        [[1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0]], [1, 0, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0], [[1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0]], 
        [[1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0]], [[1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0]], [[1, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0]], [[1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0]]]


# ========================================================================
# Test for Question 3 - Braille (Part 3)

def getTurtle():
    """This is a helper function for testing with the turtle module. It takes no inputs,
    and it returns existing turtle if there is one, otherwise makes
    a new turtle object and returns it."""
    existingTurts = turtle.turtles()
    if existingTurts == []:
        return turtle.Turtle()
    else:
        return existingTurts[0]
        
def test_draw_braille_character():
    """Testing program for the draw_braille_character function, must be visually checked"""
    
    print()
    print("--------------------------------------")
    print("Testing draw_braile_character():         CHECK VISUALLY")

    screen = turtle.Screen()
    sp = getTurtle()
    sp.speed(0)

    print("First test, braille of 'Hello, world!'")
    bs = translator("Hello, world!", braille_dictionary)
    sp.up()
    sp.goto(-200, 0)
    sp.down()
    draw_word(sp, bs)
    time.sleep(2.0)
    screen.reset()

    sp.speed(0)
    print("Second test, braille of 'People can do!'")
    bs = translator("People can do!", braille_dictionary)
    sp.up()
    sp.goto(-200, 0)
    sp.down()
    draw_word(sp, bs)
    time.sleep(2.0)
    screen.reset()


#---------------------------------------------------------------------------

if __name__ == "__main__":
    test_braille_dictionary()
    test_translator()
    test_draw_braille_character()


    True