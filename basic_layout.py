import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *

pygame.init()

size = (width, height) = (600, 400)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 155, 0)
red = (155, 0, 0)
sky = (0, 0, 40)

refw = 960
refh = 638

menubg1 = (40,48,48)
menubg2 = (200,168,72)
menubg3 = (224,216,224)
menubg4 = (40,80,104)

bg1 = (208,224,240)


clock = pygame.time.Clock()
FPS = 21

screen = pygame.display.set_mode(size)

def load_image(
    name,
    sizex=-1,
    sizey=-1,
    colorkey=None,
    ):

    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

def load_sprite_sheet(
        sheetname,
        x = -1,
        y = -1,
        sizex = -1,
        sizey = -1,
        scalex = -1,
        scaley = -1,
        colorkey = None,
        ):
    fullname = os.path.join('images',sheetname)
    sheet = pygame.image.load(fullname)
    sheet = sheet.convert()

    if x!=-1 or y!=-1 or sizex!=-1 or sizey!=-1:
        rect = pygame.Rect((x,y,sizex,sizey))
        image = pygame.Surface(rect.size)
        image = image.convert()

    else:
        image = sheet

    image.blit(sheet,(0,0),rect)
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((3,3))
        image.set_colorkey(colorkey,RLEACCEL)

    if scalex != -1 or scaley != -1:
        image = pygame.transform.scale(image,(scalex,scaley))

    return (image,image.get_rect())

def displaybg():
    pygame.draw.rect(screen, bg1, [0, 0, width, height])

    grass2, grassrect2 = load_image('grass_patch.png', int(0.6 * width), height / 5, -1)
    grassrect2.top = int(height * 0.6)
    grassrect2.left = 0
    screen.blit(grass2, grassrect2)

    pygame.draw.rect(screen,menubg1,[0,(7*height)/10,width,3*height/10])
    pygame.draw.rect(screen, menubg2, [8*width/refw, (7 * height) / 10 + 8*height/refh, width - 16*width/refw, (3 * height / 10) - 16*height/refh])
    pygame.draw.rect(screen, menubg3, [24*width/refw, (7 * height) / 10 + 20*height/refh, width - 48*width/refw, (3 * height / 10) - 40*height/refh])
    pygame.draw.rect(screen, menubg4,[32 * width / refw, (7 * height) / 10 + 28 * height / refh, width - 64 * width / refw, (3 * height / 10) - 56 * height / refh])

    grass1,grassrect1 = load_image('grass_patch.png',int(0.6*width),height/5,-1)
    grassrect1.top = int(height*0.3)
    grassrect1.left = int(0.41*width)
    screen.blit(grass1,grassrect1)

    poke1,poke1rect = load_sprite_sheet('pokemon_gen1.png',1,1,64,64,int(0.25*width),int(0.4*height),-1)
    poke1rect.left = int(0.6*width)
    poke1rect.top = int(0.15 * height)

    screen.blit(poke1,poke1rect)



def main():
    pygame.display.set_caption('Pokemon Leaf Green Battle Sequence')
    gameOver = False

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        displaybg()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

main()
