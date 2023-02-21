# -*- coding: utf-8 -*-
from zombie import Game
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        theGame = Game(timer=int(sys.argv[1]))
    else:
        theGame = Game(timer=60)