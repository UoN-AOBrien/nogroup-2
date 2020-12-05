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
FRAMERATE = 60

# Load assests
backgrounds_all = [[pygame.image.load('images/game/background/garden (low).jpeg')],
                   [pygame.image.load('images/game/background/graveyard (high).jpeg')]]
backgrounds = backgrounds_all[1]
level_img = pygame.image.load('images/game/background/graveyard (low).jpeg')
gameover_img = pygame.image.load('images/game/gameover.jpeg')

player_animations = [pygame.image.load('images/game/player/skull' + str(i) + ".png") for i in range (1, 8)]
mob_animations = [pygame.image.load('images/game/mob/mob' + str(i) + ".png") for i in range (1, 2)]

def Game(screen):
    global backgrounds_all, backgrounds    
    
    # Initialise clock
    clock = pygame.time.Clock()
    offset = pygame.time.get_ticks() // 1000

    # Initialise screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(pygame.Color("White")) 
    pygame.display.flip()
    
    # Set screen title
    pygame.display.set_caption("Game") 
    
    
    # Player group
    player_loop = 0
    player_frame = 0
    player = eng.Player(player_animations[player_frame])
    player_group = pygame.sprite.Group()
    player_group.add(player)
    
    # Bullet group one group for each bullet direction
    rightbullet_group = pygame.sprite.Group()
    leftbullet_group = pygame.sprite.Group()
    downbullet_group = pygame.sprite.Group()
    upbullet_group = pygame.sprite.Group()
    
    # Mob group
    # With adjustable number of mobs
    mob = pygame.sprite.Group()
    mob_number = 5
    for i in range(mob_number):#no of mobs
        m = eng.Mob(mob_animations[0])
        mob.add(m)
        
    # Heart group
    # With adjustable number of hearts
    heart = pygame.sprite.Group()
    heart_number = 1
    for i in range(heart_number):#no of hearts
        h = eng.Heart()
        heart.add(h)
        
    # Bullet star group
    # With adjustable number of bullet stars
    starbullet = pygame.sprite.Group()
    for i in range(1):#no of hearts
        s = eng.StarBullet()
        starbullet.add(s)  
    
    # Score and a separate variable for kill counter
    score = 0
    kills = 0
    level = 1
    
    """ Display Level Screen """
    eng.DrawLevelScreen(screen, WIDTH, HEIGHT, level_img, level)
    offset = pygame.time.get_ticks() // 1000 # set offset for game timer

    # init background
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
            scroll_bg[i] = eng.DrawScrollBackground(screen, WIDTH, speed, bg[i], FRAMERATE, scroll_bg[i])
        
        # reset loop
        if scroll_bg[1] < 0:
            scroll_bg = [0, WIDTH]
            bg[0] = bg[1]
            index = random.randint(0, len(backgrounds)-1)
            bg[1] = backgrounds[index]
        
        
        """ TIMER AND SCORE """
        # Calculates the total number of seconds at current point in time
        # Code is built from http://programarcadegames.com/python_examples/f.php?file=timer.py
        # Also calculates score based on time spent in game and number of kills
        total_seconds = (pygame.time.get_ticks() // 1000) - offset
        
        if total_seconds >= 60:
            level += 1
            eng.DrawLevelScreen(screen, WIDTH, HEIGHT, level_img, level)
            offset = pygame.time.get_ticks() // 1000 # set offset for game timer
            backgrounds = backgrounds_all[level % 2]
            
        seconds = total_seconds % 60
        if kills > 1 or kills == 1:
            score = seconds + (kills*5)
        else:
            score = seconds
        
        
        """ PLAYER MECHANICS """
        # increment player frame
        player_loop += 1
        if player_loop >= FRAMERATE // (len(player_animations) * speed):
            player_loop = 0
            player_frame += 1
        if player_frame >= len(player_animations):
            player_frame = 0
            
        # Shoots bullet on left click
        if left_click:
            rightbullet_group.add(player.create_rightbullet())
        
        # If player life is 0 game stops
        if player.life == 0:
            eng.DrawStaticBackground(screen, WIDTH, HEIGHT, gameover_img) # Set game over background
            pygame.display.flip() # update display
            pygame.time.wait(5000) # wait for 5 seconds i.e. display game over screen
            game_running = False #if player is hit by mob, loop stops and game exits
        
        """ COLLISIONS """
        # Check to see if a bullet hits a mob
        # Bullet needs to run into mob and vice versa so 2 Trues
        bullet_groups = [leftbullet_group, rightbullet_group, upbullet_group, downbullet_group]
        for bullet in bullet_groups:
            mob_hit = pygame.sprite.groupcollide(mob, rightbullet_group, True, True)
            #This loop adds a mob if a mob dies
            for hit in mob_hit: 
                m = eng.Mob(mob_animations[0])
                mob.add(m)
                kills += 1
        
        # If the player is hit by a mob the player loses a life 
        # Mob is removed to prevent too many collisions and loss of multiple lives
        player_hit = pygame.sprite.spritecollide(player, mob, True) 
        if player_hit:
            player.life -= 1
            mob.remove(m)
            m = eng.Mob(mob_animations[0])
            mob.add(m)
            
            
        """ BOOSTS """
        # If the player is touches heart gains a life
        # Heart is removed to prevent too many collisions and gaining of multiple lives
        life_up = pygame.sprite.spritecollide(player, heart, True) 
        if life_up:
            player.life += 1
            heart.remove(h)
        
        # Caps the amount of lives the player can gain
        # Spawns a new life every 20 to 30 seconds
        if player.life < 5:
            if seconds % (random.randint(20, 30)) == 0:
                heart.add(h)
        
        # If the player is touches bullet, cause bullets to shoot in 4 directions
        # Bullet is removed to prevent too many collisions and gaining of multiple, multiple bullets
        bullet_up = pygame.sprite.spritecollide(player, starbullet, True)
        if bullet_up:
            leftbullet_group.add(player.create_leftbullet())
            downbullet_group.add(player.create_downbullet())
            rightbullet_group.add(player.create_rightbullet())
            upbullet_group.add(player.create_upbullet())
            starbullet.remove(s)
            
        # Spawns a new star bullet every 30 seconds    
        if seconds%30 == 0:
            starbullet.add(s)  
            
        
        
        # Updates and draws everything to screen
        mob.update()
        player_group.update(player_animations[player_frame])
        heart.update()
        starbullet.update()
    
        mob.draw(screen)
        heart.draw(screen)
        rightbullet_group.draw(screen)
        leftbullet_group.draw(screen)
        downbullet_group.draw(screen)
        upbullet_group.draw(screen)
        player_group.draw(screen)
        starbullet.draw(screen)
    
        rightbullet_group.update()
        leftbullet_group.update()
        downbullet_group.update()
        upbullet_group.update()
            
            
    
        # Test section for timer, lives, score and kill counter 
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        lives = myfont.render(str(player.life), False, (153, 0, 153))
        timer = myfont.render(str(seconds), False, (153, 0, 153))
        score_total = myfont.render(str(score), False, (153, 0, 153))
        kills_total = myfont.render(str(kills), False, (153, 0, 153))
        
      
        screen.blit(lives,(0,0))
        screen.blit(timer,(0,750))
        screen.blit(score_total,(0,250))
        screen.blit(kills_total,(750,250))
       
        
        # Add to frame count for the timer
        clock.tick(FRAMERATE)
        pygame.display.flip()
