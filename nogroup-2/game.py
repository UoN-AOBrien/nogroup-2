# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:14:29 2020

@author: Alex
"""

import pygame
import utils.engine as eng

# Global variables
WIDTH = 1200
HEIGHT = 600
FRAMERATE = 60

# Load assests
""" LOAD GAME ASSETS HERE """

def Game(screen):
    # Initialise clock
    clock = pygame.time.Clock()

    # Initialise screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(pygame.Color("White")) 
    pygame.display.flip()
    
    pygame.display.set_caption("Game") # Set screen title
    
    game_running = True
    while game_running:
        
        # Event loop
        mouse_xpos, mouse_ypos = pygame.mouse.get_pos() # Get mouse location
        left_click, right_click = False, False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Window close event
                eng.Shutdown()
            if event.type == pygame.KEYDOWN: # Key down events
                if event.key == pygame.K_ESCAPE:
                    game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click down
                if event.button == 1:
                    left_click = True
                if event.button == 3:
                    right_click = True
                    
            # Refresh screen
            clock.tick(FRAMERATE)
            pygame.display.flip()