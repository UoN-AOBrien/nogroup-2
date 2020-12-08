# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:05:08 2020

@author: wongp
"""
import pygame
import utils.engine as eng
import random

# Global variables
WIDTH = 1600
HEIGHT = 900
FRAMERATE = 60

# Load assests


BLACK=(0,0,0)
GREEN = (0,255,0)



import pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("White")) 
pygame.display.flip()


boss_life = 20

left_click = False


while True:
   
    pygame.draw.rect(screen, BLACK ,(50, 800, 800, 50))
    pygame.draw.rect(screen, GREEN, (50, 800, (40*(boss_life)), 50))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click down
                if event.button == 1:
                    left_click = True
                    
                    
    if left_click == True:
        boss_life = boss_life - 1
        left_click = False
        
    
screen.display.flip()
        
        
        
        
        
        
        
        
        
        
        
        
