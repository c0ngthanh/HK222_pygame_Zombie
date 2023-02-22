# -*- coding: utf-8 -*-




class GameConstants:
    """
    Constants used for rendering of main game
    """

    GAMEWIDTH       = 1280
    GAMEHEIGHT      = 720
    GAMEMAXFPS      = 45


class LevelConstants:
    """
    Constants used to handle leveling
    """

    LEVELGAP        = 100 #score
    LEVELMOLESPEED  = 5 #% faster
    LEVELMOLECHANCE = 10 #% less


class HoleConstants:
    """
    Constants used in the holes
    """

    HOLEWIDTH       = 80
    HOLEHEIGHT      = int(HOLEWIDTH*(3/8))
    HOLEROWS        = 4 # !!
    HOLECOLUMNS     = 7 # !!

    # Checks
    # if HOLEHEIGHT*HOLEROWS > GameConstants.GAMEHEIGHT:
    #     raise ValueError("HOLEROWS or HOLEHEIGHT too high (or GAMEHEIGHT too small)")
    # if HOLEWIDTH*HOLECOLUMNS > GameConstants.GAMEWIDTH:
    #     raise ValueError("HOLECOLUMNS or HOLEWIDTH too high (or GAMEWIDTH too small)")


class MoleConstants:
    """
    Constants used for mole generation and calculations
    """

    MOLEWIDTH       = int( HoleConstants.HOLEWIDTH*1 )
    MOLEHEIGHT      = int(MOLEWIDTH)
    MOLEDEPTH       = 15 #% of height
    MOLECOOLDOWN    = 500 #ms

    MOLESTUNNED     = 1000 #ms
    MOLEHITHUD      = 500 #ms
    MOLEMISSHUD     = 250 #ms

    MOLECHANCE      = 1/30
    MOLECOUNT       = 8 # !!
    MOLEUPMIN       = 0.3 #s
    MOLEUPMAX       = 2 #s

    # Checks
    # if MOLECOUNT > HoleConstants.HOLEROWS*HoleConstants.HOLECOLUMNS:
    #     raise ValueError("MOLECOUNT too high")


class TextConstants:
    """
    Constants used for text rendering
    """

    TEXTTITLE       = "Zombie"
    TEXTFONTSIZE    = 30
    TEXTFONTFILE    = "assets/3rd Man.ttf"


class ImageConstants:
    """
    Constants that are image based
    """

    IMAGEBASE       = "assets/"

    IMAGEBACKGROUND = IMAGEBASE + "newBG.png"

    IMAGEMOLENORMAL = IMAGEBASE + "zombiefiles/png/male/Attack (1).png"
    IMAGEMOLEHIT    = IMAGEBASE + "zombiefiles/png/male/Dead (12).png"

    IMAGEHOLE       = IMAGEBASE + "hole.png"
    IMAGEMALLET     = IMAGEBASE + "mallet.png"


class MalletConstants:
    """
    Constants used for rendering the mallet
    """

    MALLETWIDTH     = int(HoleConstants.HOLEWIDTH)
    MALLETHEIGHT    = int(MALLETWIDTH)

    MALLETROTNORM   = 15
    MALLETROTHIT    = 30


class Constants(GameConstants, LevelConstants, HoleConstants, MoleConstants, TextConstants, ImageConstants, MalletConstants):
    """
    Stores all the constants used in the game
    """

    DEBUGMODE       = False
    LEFTMOUSEBUTTON = 1