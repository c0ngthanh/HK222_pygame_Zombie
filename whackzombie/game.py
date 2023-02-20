import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 350
HOLEWIDTH = 100
HOLEHEIGHT = 40
HAMMERWIDTH = 100
HAMMERHEIGHT = 100
FPS = 60
IMAGEBACKGROUND = pygame.image.load('img/bg1.png')
IMAGEHOLE = pygame.image.load('img/hole.png')
IMAGEHAMMER = pygame.image.load('img/hammer.png')
holes_position = [(250,100),(250,200)]

class Game:
    def __init__(self) -> None:
        #Init pygame
        pygame.init()
        #Create screen play
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('Smash Zombie')
        #Load backgroud
        self.img_background = pygame.transform.scale(IMAGEBACKGROUND, (WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.update()
        #Load hole
        self.img_hole = pygame.transform.scale(IMAGEHOLE, (HOLEWIDTH, HOLEHEIGHT))
        #Load hammer
        self.img_hammer = pygame.transform.scale(IMAGEHAMMER, (HAMMERWIDTH, HAMMERHEIGHT))
        #Loop event
        self.run()
    
    def display_loop(self, clicked):
        #Display background
        self.screen.blit(self.img_background, (0, 0))
        #Display hole
        for pos in holes_position:
            self.screen.blit(self.img_hole, pos)
        #Display hammer
        thisHammer = pygame.transform.rotate(self.img_hammer.copy(),(60 if clicked else 30))
        hammer_x, hammer_y = pygame.mouse.get_pos()
        hammer_x -= thisHammer.get_width() / 5
        hammer_y -= thisHammer.get_height() / 4
        self.screen.blit(thisHammer, (hammer_x, hammer_y))
    
    def run(self):
        self.clicked = False
        self.loop = True
        #Create loop
        while self.loop:
            #Do all loop events
            self.event_loop()
            self.display_loop(self.clicked)
            pygame.display.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.clicked = True
                print(pos)
                self.loop = False

if __name__ == '__main__':
    Game()