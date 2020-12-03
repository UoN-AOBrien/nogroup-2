# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:04:12 2020

@author: Alex
"""
# Import libraries and modules
import pygame, sys, os
import random

# Import individual contribuutions
import utils.alex as FuncAlex
import utils.harri as FuncHarri
import utils.hongyuan as FuncHongyuan
import utils.peggy as FuncPeggy

# Classes and Functions

# Shutdown application
def Shutdown():
    pygame.quit()
    sys.exit()
    os._exit()
    
def CenterWindow():
    FuncAlex.CenterWindow()

# Draw menu buttons - centered on screen (stackable)
def DrawMenuButton(window, width, height, button_number, image):
    return FuncAlex.DrawMenuButton(window, width, height, button_number, image)

# Draw static background - useful for menu screens etc
def DrawStaticBackground(window, width, height, image):
    FuncAlex.DrawStaticBackground(window, width, height, image)

    
# Draw infinite scroll
def DrawScrollBackground(window, width, speed, image, x):
    return FuncAlex.DrawScrollBackground(window, width, speed, image, x)


#%% Harri's code

""" GLOBAL VAR HARDCODED - REPLACE """
screen_width = 1600
screen_height = 900

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,100))#100pixels wide and high
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center=(screen_width/2,screen_height/2))


    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) #return bullet and has the position of wherever the mouse is
#

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255,0,0))#colour
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

    def update(self):
        self.rect.x += 5

        if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
            self.kill() #bullet will destroy itself to save memory and improve performance