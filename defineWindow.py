from screeninfo import get_monitors
import re

def defineWindow():
    WINDOW_WIDTH = getWidth()/2
    WINDOW_HEIGHT = getHeight()/2
    return WINDOW_WIDTH, WINDOW_HEIGHT

def getWidth():
    splits = str(get_monitors()).split() #splits the get_monitors() list into an array
    # for split in splits:
    #     print(split)
    toInt = re.findall(r'\b\d+\b', splits[2]) #Use regex to grab the number from array element width=####
    toInt = str(toInt[0]) #converts toInt from a list of one element to a string
    #print(toInt)
    return int(toInt) #convert toInt string to an int

def getHeight():
    splits = str(get_monitors()).split() #splits the get_monitors() list into an array
    # for split in splits:
    #     print(split)
    toInt = re.findall(r'\b\d+\b', splits[3]) #Use regex to grab the number from array element height=####
    toInt = str(toInt[0]) #converts toInt from a list of one element to a string
    #print(toInt)
    return int(toInt) #convert toInt string to an int