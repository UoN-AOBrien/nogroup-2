# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:46:22 2020

@author: Alex
"""

# Import libraries and modules
import pygame
import game
import utils.engine as eng

# Global variables
WIDTH = 1200
HEIGHT = 600
FRAMERATE = 60

# Load menu assets
""" LOAD MENU ASSETS HERE """

# Initialise modules
pygame.init()

# Initialise clock
clock = pygame.time.Clock()

# Initialise screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("Black")) 
pygame.display.flip()
      
# Application Loop
while True:
    pygame.display.set_caption("Main Menu") # Set screen title
    screen.fill(pygame.Color("Black"))
    
    # Draw main menu
    play_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 1, pygame.Color("White"))
    quit_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 5, pygame.Color("Red"))
    
    #  Event loop
    mouse_xpos, mouse_ypos = pygame.mouse.get_pos() # Get mouse location
    left_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Window close event
            eng.Shutdown()
        if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click down
            if event.button == 1:
                left_click = True
    
    # Menu button press
    if left_click:
        if play_button.collidepoint(mouse_xpos, mouse_ypos):
            game.Game(screen)
        if quit_button.collidepoint(mouse_xpos, mouse_ypos):
            eng.Shutdown()
    
    # Refresh screen
    clock.tick(FRAMERATE)
    pygame.display.flip()