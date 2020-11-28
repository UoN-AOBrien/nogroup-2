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
WIDTH = 800
HEIGHT = 600
FRAMERATE = 60

# Load menu assets
play_img = pygame.image.load('images/menu/play.png')
options_img = pygame.image.load('images/menu/options.png')
quit_img = pygame.image.load('images/menu/quit.png')
background_img = pygame.image.load('images/menu/background.png')

cheatsheet = pygame.image.load('images/cheatsheet.png')


# Initialise modules
pygame.init()

# Center screens
eng.CenterWindow()

# Initialise clock
clock = pygame.time.Clock()

# Initialise screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("Black")) 
pygame.display.flip()

# Application Loop
while True:
    pygame.display.set_caption("Main Menu") # Set screen title
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set screen mode
    eng.DrawStaticBackground(screen, WIDTH, HEIGHT, background_img) # Set menu background
    
    # Draw main menu buttons
    play_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 3, play_img)
    options_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 4, options_img)
    quit_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 5, quit_img)
    
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
            eng.DrawStaticBackground(screen, WIDTH, HEIGHT, cheatsheet)
            pygame.display.set_caption("CheatSheet")
            pygame.display.flip()
            
            
            left_click2 = False
        
            running = True
            while running:
              for event in pygame.event.get():
                  if event.type == pygame.QUIT: # Window close event
                          eng.Shutdown()
                  if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click down
                      if event.button == 1:
                          left_click2 = True   
                      if left_click2:
                          game.Game(screen)
            
        if options_button.collidepoint(mouse_xpos, mouse_ypos):
            pass
        if quit_button.collidepoint(mouse_xpos, mouse_ypos):
            eng.Shutdown()
    
    # Refresh screen
    clock.tick(FRAMERATE)
    pygame.display.flip()