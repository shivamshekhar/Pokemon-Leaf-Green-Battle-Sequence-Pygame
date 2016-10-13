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

spritemovement = int(8*width/600)

bg1 = (208,224,240)


clock = pygame.time.Clock()
FPS = 21

screen = pygame.display.set_mode(size)

def displaytext(
    text,
    fontsize,
    x,
    y,
    color,
    fontstyle='ariel'
    ):

    font = pygame.font.SysFont(fontstyle, fontsize, True)
    text = font.render(text, 1, color)
    textpos = text.get_rect(centerx=x, centery=y)
    screen.blit(text, textpos)


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
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)

    if scalex != -1 or scaley != -1:
        image = pygame.transform.scale(image,(scalex,scaley))

    return (image,image.get_rect())

def flashscreen(counter):
    flashbg = pygame.Surface((width,height))
    flashbg.fill((255,255,255))

    mul = 0

    if((counter % 255 > 45 and counter%255 < 145) or counter%255 > 190):
        mul = -4
    else:
        mul = -20

    flashbg.set_alpha((255 + mul*(counter % 255))%255)
    """if(flashbg.get_alpha() < 255):
        flashbg.set_alpha(flashbg.get_alpha() + 1)
    else:
        flashbg.set_alpha(0)"""
    screen.blit(flashbg,pygame.Rect((0,0,width,height)))

def displaydialogboxbg():

    """grass2, grassrect2 = load_image('grass_patch.png', int(0.6 * width), height / 5, -1)
    grassrect2.top = int(height * 0.6)
    grassrect2.left = 0
    screen.blit(grass2, grassrect2)
    """
    pygame.draw.rect(screen,menubg1,[0,(7*height)/10,width,3*height/10])
    pygame.draw.rect(screen, menubg2, [8*width/refw, (7 * height) / 10 + 8*height/refh, width - 16*width/refw, (3 * height / 10) - 16*height/refh])
    pygame.draw.rect(screen, menubg3, [24*width/refw, (7 * height) / 10 + 20*height/refh, width - 48*width/refw, (3 * height / 10) - 40*height/refh])
    pygame.draw.rect(screen, menubg4,[32 * width / refw, (7 * height) / 10 + 28 * height / refh, width - 64 * width / refw, (3 * height / 10) - 56 * height / refh])

    """grass1,grassrect1 = load_image('grass_patch.png',int(0.6*width),height/5,-1)
    grassrect1.top = int(height*0.3)
    grassrect1.left = int(0.41*width)
    screen.blit(grass1,grassrect1)
    """

    """poke1,poke1rect = load_sprite_sheet('pokemon_gen1.png',1,1,64,64,int(0.25*width),int(0.4*height),-1)
    poke1rect.left = int(0.6*width)
    poke1rect.top = int(0.15 * height)

    screen.blit(poke1,poke1rect)"""


class grasspatch(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1,self.rect1 = load_image('grass_patch.png',int(0.6*width),height/5,-1)
        self.rect1.top = int(height*0.3)
        self.rect1.left = (-1*self.rect1.width)
        self.movement1 = [spritemovement,0]

        self.image2, self.rect2 = load_image('grass_patch.png', int(0.6 * width), height / 5, -1)
        self.rect2.top = int(height * 0.6)
        self.rect2.left = width
        self.movement2 = [-spritemovement,0]

        self.ismoving = True

    def update(self):
        if self.ismoving:
            self.rect1 = self.rect1.move(self.movement1)
            self.rect2 = self.rect2.move(self.movement2)

            if self.rect1.left > int(0.41*width) or self.rect2.left < 1:
                self.ismoving = False

    def draw(self):
        screen.blit(self.image1,self.rect1)
        screen.blit(self.image2,self.rect2)


class wildpokemon(pygame.sprite.Sprite):
    def __init__(self,num):
        pygame.sprite.Sprite.__init__(self)
        self.num = num
        self.x = int((num-1)/10)
        self.y = num - (self.x)*10
        self.image,self.rect = load_sprite_sheet('pokemon_gen1.png', 161*(self.y - 1), int(1 + 65.6*(self.x)),65,65,int(0.23*width),int(0.345*height),-1)
        self.rect.left = int((-1*self.rect.width)*2)
        self.rect.top = int(0.14 * height)
        self.movement = [spritemovement,0]
        self.ismoving = True

    def update(self):
        if self.ismoving:
            self.rect = self.rect.move(self.movement)
            if self.rect.left > int(0.55*width):
                self.ismoving = False

    def draw(self):
        screen.blit(self.image,self.rect)

class playerpokemon(pygame.sprite.Sprite):
    def __init__(self,num):
        pygame.sprite.Sprite.__init__(self)
        self.num = num
        self.x = int((num - 1) / 10)
        self.y = num - (self.x) * 10

        self.image,self.rect = load_sprite_sheet('pokemon_gen1.png',65 + 161*(self.y - 1),int(1 + 65.6*(self.x)),65,65,int(0.23*width),int(0.345*height),-1)
        self.rect.left = int(width*1.1)
        self.rect.top = int(0.44 * height)
        self.movement = [-spritemovement,0]
        self.ismoving = True

    def update(self):
        if self.ismoving:
            self.rect = self.rect.move(self.movement)
            if self.rect.left < int(0.1*width):
                self.ismoving = False

    def draw(self):
        screen.blit(self.image,self.rect)

def main():
    pygame.display.set_caption('Pokemon Leaf Green Battle Sequence')
    gameOver = False
    battleStart = False
    titlescreen = True

    titlebg,titlebgrect = load_image('bg_wallpaper.jpg',width,height)
    logo,logorect = load_image('logo.png',width/2,int(height*0.4),-1)
    logorect.left = width/2 - logorect.width/2
    logorect.top = height/50
    venu,venurect = load_image('venusaur_sillhoute.jpg',int(width/2),int(height/2),-1)
    venurect.left = int(width / 2 - venurect.width*0.4 )
    venurect.top = int(height*0.4)

    menuselect = 0
    ismenuselect = False

    counter = 0

    bg_music = pygame.mixer.Sound('sounds/wild_pokemon_appears.ogg')
    title_music = pygame.mixer.Sound('sounds/opening.ogg')

    wildPokemon = wildpokemon(1)
    mypokemon = playerpokemon(48)
    grass = grasspatch()

    title_music.play(-1)

    while not gameOver:
        while titlescreen:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN:
                    titlescreen = False
                    battleStart = True
                    title_music.stop()
                    bg_music.play(-1)

            screen.blit(titlebg,titlebgrect)
            flashscreen(counter)
            screen.blit(logo,logorect)
            screen.blit(venu, venurect)
            displaytext('Written By : Shivam Shekhar',int(0.0267*width),width/7,height - height/60,(255,255,255))

            counter = counter + 1
            pygame.display.update()
            clock.tick(FPS)

        while battleStart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            pygame.draw.rect(screen, bg1, [0, 0, width, height])

            grass.draw()
            mypokemon.draw()
            displaydialogboxbg()
            wildPokemon.draw()


            wildPokemon.update()
            mypokemon.update()
            grass.update()

            pygame.display.update()
            clock.tick(FPS)
    pygame.quit()
    quit()

main()