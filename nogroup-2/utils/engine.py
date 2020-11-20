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
def Shutdown():
    pygame.quit()
    sys.exit()
    os._exit()

def DrawMenuButton(window, width, height, button_number, image):
    return FuncAlex.DrawMenuButton(window, width, height, button_number, image)

def DrawMenuBackground(window, width, height, image):
    FuncAlex.DrawMenuBackground(window, width, height, image)
