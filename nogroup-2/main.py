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

cheatsheet_img = pygame.image.load('images/cheatsheet.png')

bgmusic_img = pygame.image.load('images/menu/options/bgmusic.png')
bgmusicoff_img = pygame.image.load('images/menu/options/bgmusicoff.png')



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

bg_on = True
pygame.mixer.music.load('sound/example.mp3')
pygame.mixer.music.play(-1)

screen_flag = "main_menu"

    

# Application Loop
while True:
   
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set screen mode
    
    if screen_flag == "main_menu":
        pygame.display.set_caption("Main Menu") # Set screen title
        eng.DrawStaticBackground(screen, WIDTH, HEIGHT, background_img) # Set menu background
        
        # Draw main menu buttons
        play_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 3, play_img)
        options_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 4, options_img)
        quit_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 5, quit_img)
    
    
    elif screen_flag == "options":
        pygame.display.set_caption("Options")
        eng.DrawStaticBackground(screen, WIDTH, HEIGHT, background_img)
        
        if bg_on == True:
            bgmusic_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 3, bgmusic_img)
        elif bg_on == False:
            bgmusic_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 3, bgmusicoff_img)
            
        options_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 4, options_img)
        
    elif screen_flag == "cheat_sheet":
        eng.DrawStaticBackground(screen, WIDTH, HEIGHT, cheatsheet_img) 
        pygame.display.set_caption("Cheat Sheet")
        play_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 3, play_img)
        
    elif screen_flag == "game":
        game.Game(screen)
        
    
        
    mouse_xpos, mouse_ypos = pygame.mouse.get_pos() # Get mouse location
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Window close event
            eng.Shutdown()
        if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click down
            if event.button == 1:
                if screen_flag == "main_menu":
                    if play_button.collidepoint(mouse_xpos, mouse_ypos):
                        screen_flag = "cheat_sheet"
                    if options_button.collidepoint(mouse_xpos, mouse_ypos):
                        screen_flag = "options"
                    if quit_button.collidepoint(mouse_xpos, mouse_ypos):
                        eng.Shutdown()
                        
                elif screen_flag == "cheat_sheet":
                    if play_button.collidepoint(mouse_xpos, mouse_ypos):
                        screen_flag = "game"
                        
                elif screen_flag == "options":
                    if options_button.collidepoint(mouse_xpos, mouse_ypos):
                        screen_flag = "main_menu"
                    if bgmusic_button.collidepoint(mouse_xpos, mouse_ypos):
                        if bg_on == True: 
                                pygame.mixer.music.pause()
                                bg_on = False
                        else:
                            pygame.mixer.music.load('sound/example.mp3')
                            pygame.mixer.music.play(-1)
                            bg_on = True
                        

    clock.tick(FRAMERATE)
    pygame.display.flip()   
            
 