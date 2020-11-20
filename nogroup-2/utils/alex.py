# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:49:06 2020

@author: Alex
"""
# Import libraries and modules
import pygame

# Import individual contribuutions
import utils.harri as FuncHarri
import utils.hongyuan as FuncHongyuan
import utils.peggy as FuncPeggy



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

def DrawMenuBackground(window, width, height, image):
    backgroundRect = pygame.Rect(0, 0, width, height)
    image = pygame.transform.scale(image, (width, height))
    window.blit(image, backgroundRect)

