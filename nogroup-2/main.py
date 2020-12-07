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
play_img = pygame.image.load('images/menu/play.jpeg')
options_img = pygame.image.load('images/menu/options.jpeg')
quit_img = pygame.image.load('images/menu/quit.jpeg')
background_img = pygame.image.load('images/menu/background.png')

cheatsheet_img = pygame.image.load('images/cheatsheet.png')

bgmusic_img = pygame.image.load('images/menu/options/bgmusic.jpeg')
bgmusicoff_img = pygame.image.load('images/menu/options/bgmusicoff.jpeg')
back_img = pygame.image.load('images/menu/options/back.jpeg')





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
pygame.mixer.music.load('sound/longspookydogmusic.mp3')
pygame.mixer.music.play(-1)

menu_sound = pygame.mixer.Sound("sound/music for game/spookymenubuttonpress.mp3")   










screen_flag = "main_menu"

    

# Application Loop
while True:
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set screen mode
    pygame.mouse.set_visible(True) # Ensure mouse is visible
    
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
            
        options_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 4, back_img)
        
    elif screen_flag == "cheat_sheet":
        eng.DrawStaticBackground(screen, WIDTH, HEIGHT, cheatsheet_img) 
        pygame.display.set_caption("Cheat Sheet")
        play_button = eng.DrawMenuButton(screen, WIDTH, HEIGHT, 5.3, play_img)
        
    elif screen_flag == "game":
        screen_flag = "main_menu"
        game.Game(screen)
        
    
        
    mouse_xpos, mouse_ypos = pygame.mouse.get_pos() # Get mouse location
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Window close event
            eng.Shutdown()
        if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click down
            if event.button == 1:
                if screen_flag == "main_menu":
                    if play_button.collidepoint(mouse_xpos, mouse_ypos):
                        pygame.mixer.Sound.play(menu_sound)
                        screen_flag = "cheat_sheet"
                    if options_button.collidepoint(mouse_xpos, mouse_ypos):
                        pygame.mixer.Sound.play(menu_sound)
                        screen_flag = "options"
                    if quit_button.collidepoint(mouse_xpos, mouse_ypos):
                        eng.Shutdown()
                        
                elif screen_flag == "cheat_sheet":
                    if play_button.collidepoint(mouse_xpos, mouse_ypos):
                        pygame.mixer.Sound.play(menu_sound)
                        screen_flag = "game"
                        
                elif screen_flag == "options":
                    if options_button.collidepoint(mouse_xpos, mouse_ypos):
                        pygame.mixer.Sound.play(menu_sound)
                        screen_flag = "main_menu"
                    if bgmusic_button.collidepoint(mouse_xpos, mouse_ypos):
                        pygame.mixer.Sound.play(menu_sound)
                        if bg_on == True: 
                                pygame.mixer.music.pause()
                                bg_on = False
                        else:
                            pygame.mixer.music.load('sound/example.mp3')
                            pygame.mixer.music.play(-1)
                            bg_on = True
                        

    clock.tick(FRAMERATE)
    pygame.display.flip()   
            
 