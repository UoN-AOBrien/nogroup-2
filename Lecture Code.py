# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:40:39 2020

@author: Alex
"""

import pygame
import os

# Global variables
WIDTH = 1200
HEIGHT = 600
BORDER = 40

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill(pygame.Color("blue"))

Rect1 = pygame.Rect(0, 0, WIDTH, BORDER)
Rect2 = pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER)
Rect3 = pygame.Rect(0, 0, BORDER, HEIGHT)

pygame.draw.rect(screen, pygame.Color("White"), Rect1)
pygame.draw.rect(screen, pygame.Color("White"), Rect2)
pygame.draw.rect(screen, pygame.Color("White"), Rect3)

pygame.display.flip()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

pygame.quit() # for the rest of people with windows or Linux
os._exit() # for MAC users