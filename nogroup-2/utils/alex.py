# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:49:06 2020

@author: Alex
"""
# Import libraries and modules
import pygame
import os
import random


# Center window function - os function call 
def CenterWindow():
    os.environ['SDL_VIDEO_CENTERED'] = '1'

# Draw menu buttons - center of window (stackabele)
def DrawMenuButton(window, width, height, button_number, image):
    XDIVISOR = 2
    YDIVISOR = 11

    button_width = width//XDIVISOR
    button_height = height//YDIVISOR
    
    x = width//2 - button_width//2
    y = (2 * button_height * button_number) - button_height
    
    buttonRect = pygame.Rect(x, y, button_width, button_height)
    image = pygame.transform.scale(image, (button_width, button_height))
    window.blit(image, buttonRect)
    
    return buttonRect

# Draw static background - menu screens etc
def DrawStaticBackground(window, width, height, image):
    backgroundRect = pygame.Rect(0, 0, width, height)
    image = pygame.transform.scale(image, (width, height))
    window.blit(image, backgroundRect)

# Draw infinite scroll
def DrawScrollBackground(window, width, speed, image, x):
    x -= speed
    window.blit(image, (x, 0))
    return x
        