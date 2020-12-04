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
    
    
    # Player group
    player = eng.Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)
    
    # Bullet group
    #bullet group
    rightbullet_group = pygame.sprite.Group()
    leftbullet_group = pygame.sprite.Group()
    downbullet_group = pygame.sprite.Group()
    upbullet_group = pygame.sprite.Group()
    
    #mob group
    mob = pygame.sprite.Group()
    mob_number = 5
    for i in range(mob_number):#no of mobs
        m = eng.Mob()
        mob.add(m)
        
    #heart group
    heart = pygame.sprite.Group()
    heart_number = 1
    for i in range(heart_number):#no of hearts
        h = eng.Heart()
        heart.add(h)
        
    
    starbullet = pygame.sprite.Group()
    for i in range(1):#no of hearts
        s = eng.StarBullet()
        starbullet.add(s)  
    
        
    frame_count = 0
    frame_rate = 120
    
    
    score = 0
    kills = 0


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
        
        
        """ TIMER AND SCORE """
        total_seconds = frame_count // frame_rate
        seconds = total_seconds % 60
        if kills > 1 or kills == 1:
            score = seconds + (kills*5)
        else:
            score = seconds
        
        
        """ PLAYER MECHANICS """
        if left_click:
            rightbullet_group.add(player.create_rightbullet())
            
        if player.life == 0:
            game_running = False #if player is hit by mob, loop stops and game exits
            eng.Shutdown()
        else:
            game_running = True  
        
        """ COLLISIONS """
        #check to see if a bullet hits a mob
        mob_hit = pygame.sprite.groupcollide(mob, rightbullet_group, True, True)#bullet needs to run into mob and vice versa so 2 Trues
        for hit in mob_hit: #this loop adds a mob if a mob dies
            m = eng.Mob()
            mob.add(m)
            kills = kills + 1
            
        mob_hit = pygame.sprite.groupcollide(mob, leftbullet_group, True, True)#bullet needs to run into mob and vice versa so 2 Trues
        for hit in mob_hit: #this loop adds a mob if a mob dies
            m = eng.Mob()
            mob.add(m)
            kills = kills + 1
            
        mob_hit = pygame.sprite.groupcollide(mob, downbullet_group, True, True)#bullet needs to run into mob and vice versa so 2 Trues
        for hit in mob_hit: #this loop adds a mob if a mob dies
            m = eng.Mob()
            mob.add(m)
            kills = kills + 1
            
        mob_hit = pygame.sprite.groupcollide(mob, upbullet_group, True, True)#bullet needs to run into mob and vice versa so 2 Trues
        for hit in mob_hit: #this loop adds a mob if a mob dies
            m = eng.Mob()
            mob.add(m)
            kills = kills + 1
            
            
        player_hit = pygame.sprite.spritecollide(player, mob, True) #hit list if player was hit
        if player_hit:
            player.life = player.life -1
            mob.remove(m)
            m = eng.Mob()
            mob.add(m)
            
            
            
            
        """ BOOSTS """
        life_up = pygame.sprite.spritecollide(player, heart, True) #hit list if player was hit
        if life_up:
            player.life = player.life + 1
            heart.remove(h)
        
        if player.life < 4:
            if seconds%30 == 0:
                heart.add(h)
        
    
    
            
            
        if seconds%30 == 0:
            starbullet.add(s)  
            
        bullet_up = pygame.sprite.spritecollide(player, starbullet, True) #hit list if player was hit
        if bullet_up:
            leftbullet_group.add(player.create_leftbullet())
            downbullet_group.add(player.create_downbullet())
            rightbullet_group.add(player.create_rightbullet())
            upbullet_group.add(player.create_upbullet())
            starbullet.remove(s)
        
        
        
        

        mob.update()
        player_group.update()
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
            
            
       
        
        
    
        
        
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        lives = myfont.render(str(player.life), False, (153, 0, 153))
        timer = myfont.render(str(seconds), False, (153, 0, 153))
        score_total = myfont.render(str(score), False, (153, 0, 153))
        kills_total = myfont.render(str(kills), False, (153, 0, 153))
        
      
        screen.blit(lives,(0,0))
        screen.blit(timer,(0,750))
        screen.blit(score_total,(0,250))
        screen.blit(kills_total,(750,250))
       
        
        
        frame_count = frame_count + 1
        clock.tick(120)
        pygame.display.flip()
