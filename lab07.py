'''Author: Eric Adjei Appiah
CS 151 Section: B
Fall 2022
Date: 10th November, 2022
'''


# I am going to leave this file a bit more stripped down than earlier assignments.
# It is your task to include the spacing, question markers, etc.  I have
# provided a section for import statements and a section for function definitions,
# and leave everything else up to you.
# """

# -----------------
#Put your import statements below
import turtle



# Global variables that store the location of files.
# Change these to match the relative addresses of the files on your computer
TEST_WORD_FILENAME = "lab7TextFiles/test-words.txt"


#---------------------------------
# Put function definitions here



# ==============================================================
# Question 1
#This is where your translator function goes
#def translator(string,braille_dict):
    

def addNumbers(bd):
    '''Add numbers and their corresponding braille characters to bd dictionary '''
    bd['1'] = [1, 0, 0, 0, 0, 0]
    bd['2'] = [1, 1, 0, 0, 0, 0]
    bd['3'] = [1, 0, 0, 1, 0, 0]
    bd['4'] = [1, 0, 0, 1, 1, 0]
    bd['5'] = [1, 0, 0, 0, 1, 0]
    bd['6'] = [1, 1, 0, 1, 0, 0]
    bd['7'] = [1, 1, 0, 1, 1, 0]
    bd['8'] = [1, 1, 0, 0, 1, 0]
    bd['9'] = [0, 1, 0, 1, 0, 0]
    bd['0'] = [0, 1, 0, 1, 1, 0]

def addLetters(bd):
    '''Add letters and their corresponding braille characters to bd dictionary '''
    bd['a'] = [1, 0, 0, 0, 0, 0]
    bd['b'] = [1, 1, 0, 0, 0, 0]
    bd['c'] = [1, 0, 0, 1, 0, 0]
    bd['d'] = [1, 0, 0, 1, 1, 0]
    bd['e'] = [1, 0, 0, 0, 1, 0]
    bd['f'] = [1, 1, 0, 1, 0, 0]
    bd['g'] = [1, 1, 0, 1, 1, 0]
    bd['h'] = [1, 1, 0, 0, 1, 0]
    bd['i'] = [0, 1, 0, 1, 0, 0]
    bd['j'] = [0, 1, 0, 1, 1, 0]

    bd['k'] = [1, 0, 1, 0, 0, 0]
    bd['l'] = [1, 1, 1, 0, 0, 0]
    bd['m'] = [1, 0, 1, 1, 0, 0]
    bd['n'] = [1, 0, 1, 1, 1, 0]
    bd['o'] = [1, 0, 1, 0, 1, 0]
    bd['p'] = [1, 1, 1, 1, 0, 0]
    bd['q'] = [1, 1, 1, 1, 1, 0]
    bd['r'] = [1, 1, 1, 0, 1, 0]
    bd['s'] = [0, 1, 1, 1, 0, 0]
    bd['t'] = [0, 1, 1, 1, 1, 0]

    bd['u'] = [1, 0, 1, 0, 0, 1]
    bd['v'] = [1, 1, 1, 0, 0, 1]
    bd['x'] = [1, 0, 1, 1, 0, 1]
    bd['y'] = [1, 0, 1, 1, 1, 1]
    bd['z'] = [1, 0, 1, 0, 1, 1]

    bd['w'] = [0, 1, 0, 1, 1, 1]

braille_dictionary = {}
braille_dictionary[" "] = [0, 0, 0, 0, 0, 0]
addNumbers(braille_dictionary)
addLetters(braille_dictionary)

# ---- Upgrade braille_dictionary from a grade 1 dictionary to a grade 2 ----


#this is where your addCommon function goes 
def addCommon(bd):
    '''Add words and their corresponding braille characters to bd dictionary '''
    bd['but']=[1, 1, 0, 0, 0, 0]
    bd['can']=[1, 0, 0, 1, 0, 0]
    bd['do']=[1, 0, 0, 1, 1, 0]
    bd['every']=[1, 0, 0, 0, 1, 0]
    bd['from']=[1, 1, 0, 1, 0, 0]
    bd['go']= [1, 1, 0, 1, 1, 0]
    bd['have']= [1, 1, 0, 0, 1, 0]
    bd['just']= [0, 1, 0, 1, 1, 0]
    bd['knowledge']=[1, 0, 1, 0, 0, 0]
    bd['like']=[1, 1, 1, 0, 0, 0]
    bd['more']=[1, 0, 1, 1, 0, 0]
    bd['not']=[1, 0, 1, 1, 1, 0]
    bd['people']=[1, 1, 1, 1, 0, 0]
    bd['quite']=[1, 1, 1, 1, 1, 0]
    bd['rather']=[1, 1, 1, 0, 1, 0]
    bd['so']=[0, 1, 1, 1, 0, 0]
    bd['that']=[0, 1, 1, 1, 1, 0]
    bd['us']=[1, 0, 1, 0, 0, 1]
    bd['very']=[1,1,1,0,0,1]
    bd['it']=[1, 0, 1, 1, 0, 1]
    bd['you']=[1, 0, 1, 1, 1, 1]
    bd['as']=[1, 0, 1, 0, 1, 1]
    bd['will']=[0, 1, 0, 1, 1, 1]
#test call to addCommon goes here
addCommon(braille_dictionary)

# ==============================================================
# Question 2

def print_braille(lst):
    '''Removes braille characters from list'''
    line1 = ""
    line2 = ""
    line3 = ""
    for item in lst:
        if isinstance(item[0], list):
            for next in item:
                line1 = line1 + str(next[0]) + " "
                line2 = line2 + str(next[1]) + " "
                line3 = line3 + str(next[2]) + " "
                line1 = line1 + str(next[3]) + " "
                line2 = line2 + str(next[4]) + " "
                line3 = line3 + str(next[5]) + " "
        elif isinstance(item[0], int):
            line1 = line1+ str(item[0]) + " "
            line2 = line2+ str(item[1]) + " "
            line3 = line3+ str(item[2]) + " "
            line1 = line1+ str(item[3]) + " "
            line2 = line2+ str(item[4]) + " "
            line3 = line3+ str(item[5]) + " "
        else:
            assert "Error in braille string"
    print(line1)
    print(line2)
    print(line3)

# ---------------------- Complete this function -----------------------------
def translator(str, bd):
    '''Converts characters into their corresponding braille character nested list'''
    res = []
    str_list = str.lower().split()
    for key in str_list:
        if key in bd:
            res.append(bd[key])
        else:
            list1 = []
            for j in key:
                if j in bd:
                    list1.append(bd[j])
            res.append(list1)

    return res






# ==============================================================
# Question 3

def draw_word(trt, lst):
    '''Drwas braille on the turtle screen'''
    for item in lst:
        if isinstance(item[0], list):
            for next in item:
                draw_braille_character(trt, next)
        elif isinstance(item[0], int):
            draw_braille_character(trt, item)
        else:
            assert "Error in braille string"

# ------------------ You're to modify this one... ---------------------------
def draw_braille_character(trt, bc):
    '''Drwas braille on the turtle screen'''
    radius = 5
    trt.setheading(0)
    trt.penup()
    trt.forward(radius)
    trt.setheading(270)
    trt.pendown()
    for i in range(len(bc)):
        if bc[i]:
            trt.fillcolor("black")
            trt.begin_fill()
        trt.circle(radius)
        if bc[i]:
            trt.end_fill()
            trt.fillcolor("white")
        trt.up()
        if i % 3 == 2:
            trt.backward(6*radius)
            trt.left(90)
            trt.forward(3*radius)
            trt.right(90)
        else:
            trt.forward(3*radius)
        trt.down()


#---------------------------------
# Put testing calls here

if __name__ == '__main__':
    print("My tests:")

    ## Put test calls to Question 2 here
    word_list1 = translator("Hello world!", braille_dictionary)
    braille_string = translator("Hi", braille_dictionary) 
    print(braille_string)
    
    print(word_list1)
    print_braille(word_list1)
    word_list2 = translator("knowledge", braille_dictionary)
    print(word_list2)
    print_braille(word_list2)

    ## Put test calls to Question 3 here
    win = turtle.Screen()
    trt = turtle.Turtle()
    trt.speed(0)
    trt.ht()
    draw_braille_character(trt, braille_dictionary["a"])
    draw_braille_character(trt, braille_dictionary["z"])
    draw_braille_character(trt, braille_dictionary["knowledge"])
    win.exitonclick()

    