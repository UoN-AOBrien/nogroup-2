# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:04:12 2020

@author: Alex
"""
# Import libraries and modules
import pygame
import sys
import os

# Classes and Functions
def Shutdown():
    pygame.quit()
    sys.exit()
    os._exit()

def DrawMenuButton(window, width, height, button_number, colour):
    x = width // 20
    y = height // 20
    z = 3 * button_number * y
    
    button = pygame.Rect(x, z, 4*x, 2*y)
    pygame.draw.rect(window, colour, button)
    
    return button
