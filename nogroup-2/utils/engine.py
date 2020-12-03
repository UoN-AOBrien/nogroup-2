# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:04:12 2020

@author: Alex
"""
# Import libraries and modules
import pygame
import sys
import os

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

def setup_sprites(width, height):
    return FuncHarri.setup_sprites(width, height)

def draw_sprites(player_group,mob,bullet_group,player,screen):
    return FuncHarri.draw_sprites(player_group,mob,bullet_group,player,screen)

