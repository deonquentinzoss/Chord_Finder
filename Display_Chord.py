#!/usr/bin/python3
###############################################################################
# Author: Deon Zoss
# Date: 20210529
# Purpose: Ascii-based display showing how to play a provided chord
#
# Example: The following output shows how to play a D-chord
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
# Example: The same D-chord, with an alternative display
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
#                          D    
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
def buildKeys(startKey,numKeys):

    WHITE_KEY=["|    ",\
               "|    ",\
               "|    ",\
               "|    ",\
               "|    ",\
               "|    ",\
               "|    ",\
               "|  X ",\
               "|____"];

    BLACK_KEY=["###",\
               "###",\
               "###",\
               "###",\
               "###",\
               " | ",\
               " | ",\
               " | ",\
               "_|_"];

###############################################################################
def getArgs():
    parser = argparse.ArgumentParser( \
             description='Ascii-based display showing'\
                         ' how to play a provided chord');
    parser.add_argument('-S','--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args();
    return args;

###############################################################################
def main():
    args = getArgs();

    #for index in range(len(WHITE_KEY)):
    #    print(WHITE_KEY[index]+BLACK_KEY[index]);
    
    print(repr(Keys.D));


if __name__ == "__main__":
    main()
