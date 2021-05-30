#!/usr/bin/python3
###############################################################################
# Author: Deon Zoss
# Date: 20210529
# Purpose: Ascii-based display showing how to play a provided chord
#
# Example: The following output shows how to play a D-major
#
#      |    ###   ###    |    ###   ###   ###    |
#      |    ###   ###    |    ###   ###   ###    |
#      |    ###   ###    |    ###   ###   ###    |
#      |    ###   ###    |    ###   ###   ###    |
#      |    ###   ###    |    ###   ###   ###    |
#      |    ###   ###    |    ###   ###   ###    |
#      |     |     |     |     |     |     |     |
#      |     |     |     |     |     |     |     |
#      |  C  |  D  |  E  |  F  |  G  |  A  |  B  |
#      |_____|_____|_____|_____|_____|_____|_____|
#  D:           X              X        X 
#
# Example: The same D-major chord, with an alternative display
#
#      |    | |###| |    |    |#|   | |###| |    |
#      |    | |###| |    |    |#|   | |###| |    |
#      |    | |###| |    |    |#|   | |###| |    |
#      |    | |###| |    |    |#|   | |###| |    |
#      |    | |###| |    |    |#|   | |###| |    |
#      |    |_|###|_|    |    |#|   |_|###|_|    |
#      |     |#####|     |     |     |#####|     |
#      |     |#####|     |     |     |#####|     |
#      |  C  |# D #|  E  |  F  |  G  |# A #|  B  |
#      |_____|#####|_____|_____|_____|#####|_____|
#                           D    
#
###############################################################################
import argparse;
from enum import Enum;

###############################################################################
class Keys(Enum):

    C  = 1;
    Db = 2;
    D  = 3;
    Eb = 4;
    E  = 5;
    F  = 6;
    Gb = 7;
    G  = 8;
    Ab = 9;
    A  = 10;
    Bb = 11;
    B  = 12;

###############################################################################
def buildKeys(startKey,numTotalKeys):
    
    currentKey=startKey.value;
    currentNumDisplayed=0;
    display=[];

    while(currentNumDisplayed < numTotalKeys):

        display = addKeytoDisplay(currentKey,display);

        if currentKey==len(Keys):
            currentKey=1;
        else:
            currentKey+=1;

        currentNumDisplayed+=1;

    for row in display:
        print(row);
    
def addKeytoDisplay(currentKey,display):    

    WHITE_KEY_VALUES=[1,3,5,6,8,10,12];

    WHITE_KEY=["   ",\
               "   ",\
               "   ",\
               "   ",\
               "   ",\
               "   ",\
               "   ",\
               " X ",\
               "___"];

    WHITE_SEPARATOR=[" | ",\
                     " | ",\
                     " | ",\
                     " | ",\
                     " | ",\
                     " | ",\
                     " | ",\
                     " | ",\
                     "_|_"];

    BLACK_KEY=["##",\
               "##",\
               "##",\
               "##",\
               "##",\
               "| ",\
               "| ",\
               "| ",\
               "|_"];

    BLACK_SEPARATOR=["#",\
                     "#",\
                     "#",\
                     "#",\
                     "#",\
                     " ",\
                     " ",\
                     " ",\
                     "_"];

    if currentKey in WHITE_KEY_VALUES:
        COLOR = "WHITE";
    else:
        COLOR = "BLACK";

    if display == []:
        if COLOR == "WHITE":
            display = WHITE_SEPARATOR.copy();
        else:
            display = BLACK_SEPARATOR.copy();
    
    if COLOR == "WHITE":
        for row in range(len(WHITE_KEY)):
            display[row]+=WHITE_KEY[row];
        if ((currentKey+1)%len(Keys)) in WHITE_KEY_VALUES:
            for row in range(len(WHITE_KEY)):
                display[row]+=WHITE_SEPARATOR[row];
        else:
            for row in range(len(BLACK_KEY)):
                display[row]+=BLACK_SEPARATOR[row];
    else:
        for row in range(len(BLACK_KEY)):
            display[row]+=BLACK_KEY[row];

        

    return display;

###############################################################################
def getArgs():
    parser = argparse.ArgumentParser( \
             description='Ascii-based display showing'\
                         ' how to play a provided chord');
    parser.add_argument('-S','--start-key', dest='startKey', default='C',
                        help='The musical note to start the display on,'\
                             ' choose from {C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B}'\
                             ' (Default is C)');
    args = parser.parse_args();
    return args;

###############################################################################
def main():
    args = getArgs();

    #for index in range(len(WHITE_KEY)):
    #    print(WHITE_KEY[index]+BLACK_KEY[index]);
    
    buildKeys(Keys[args.startKey],15);


if __name__ == "__main__":
    main()
