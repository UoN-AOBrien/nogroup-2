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



def DrawMenuButton(window, width, height, button_number, colour):
    x = width // 20
    y = height // 20
    z = 3 * button_number * y
    
    button = pygame.Rect(x, z, 4*x, 2*y)
    pygame.draw.rect(window, colour, button)
    
    return button