# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:14:29 2020

@author: Alex
"""

import pygame
import utils.engine as eng
import random

# Global variables
WIDTH = 1600
HEIGHT = 900
FRAMERATE = 120

# Load assests
backgrounds = [pygame.image.load('images/game/background/background1.png'),
              pygame.image.load('images/game/background/background2.png')]




def Game(screen):       
    # Initialise clock
    clock = pygame.time.Clock()

    # Initialise screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(pygame.Color("White")) 
    pygame.display.flip()
    
    pygame.display.set_caption("Game") # Set screen title
    
    
    
    
    scroll_bg = [0, WIDTH]
    bg=[0, 0]
    for i in range(2):
        index = random.randint(0, len(backgrounds)-1)
        bg[i] = backgrounds[index]
    
    speed = 2
    
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
                    
        
        """ SCROLL BACKGROUND """
        for i in range(2):
            scroll_bg[i] = eng.DrawScrollBackground(screen, WIDTH, speed, bg[i], scroll_bg[i])
        
        # reset loop
        if scroll_bg[1] < 0:
            scroll_bg = [0, WIDTH]
            bg[0] = bg[1]
            index = random.randint(0, len(backgrounds)-1)
            bg[1] = backgrounds[index]

        player_group, mob, bullet_group,player,screen = eng.setup_sprites(WIDTH, HEIGHT)
        player_group, bullet_group, mob = eng.draw_sprites(player_group,mob,bullet_group,player,screen)
        player_group.draw(screen)
        bullet_group.draw(screen)
        mob.draw(screen)
        # Refresh screen
        clock.tick(FRAMERATE)
        pygame.display.flip()