import os

import pygame
#import pygame.locals
from pygame.locals import *

def main():
    screen = pygame.display.set_mode((1024, 768))
    '''
    You can call set_mode during your game to switch from windowed 
        (the default) to full-screen. Other display mode flags (you just | 
        them together):
    DOUBLEBUF must be used for smooth animation
    OPENGL lets you draw 3d scenes with PyOpenGL, but won't let you perform
        most pygame drawing functions.
    There is an optional bit depth flag, but it's almost always better to 
        not include it and go with whatever platform default is available.
    If you're using DOUBLEBUF then you'll need to flip the screen after 
        you've rendered it. This is as simple as:

        >>> pygame.display.flip()
    '''    
    #screen = pygame.display.set_mode((1024, 768), WINDOWED)
    #screen = pygame.display.set_mode((1024, 768), WINDOWED | DOUBLEBUF)
    img = pygame.image.load('resources/Car_6a.png')
    xpos = 50
    ypos = 100
    screen.blit(img, (xpos, ypos))
    redraw()
    stillPlaying = True
    while (stillPlaying):
        #blank the screen
        screen.fill((0,0,0))
        xpos += 50
        screen.blit(img, (xpos, ypos))
        redraw()
        if xpos >= 700:
            invalidResponse = True
            while (invalidResponse):
                answer = raw_input("Start a new game? (y/n): ")
                #TODO: refactor below into same function as above (how to 
                # do byref/byval in python
                if answer == 'y' or answer == 'Y':
                    xpos = 50
                    ypos = 100
                    invalidResponse = False
                elif answer == 'n' or answer == 'N':
                    stillPlaying = False
                    invalidResponse = False
                else:
                    print("Please type 'y' or 'n'.")

    print("Later!")

def redraw():
    pygame.display.flip()

def evaluateHand(cards):
    return sum(cards)


def startGame():
    print
    gameOver = "Game Over."
    name = raw_input("What... is your name?\n> ")
    if name.lower() != os.getenv("USER"):
        print
        raw_input(gameOver)
        print
        return

    print
    quest = raw_input("What... is your quest?\n> ")
    if quest == '':
        print
        raw_input(gameOver)
        print
        return

    print
    question = "What... is the airspeed velocity of an unladen swallow?\n> "
    airspeed = raw_input(question)
    if airspeed.lower() != 'an african or european swallow?':
        print
        raw_input(gameOver)
        print
        return

    print
    raw_input("What? I... I don't know that...")
    print
    raw_input("Arrrrrrrrrggggggh")
    print
    raw_input("You win! How do you know so much about swallows?")
    print
    raw_input(gameOver)
    print

if __name__ == '__main__':
    main()
