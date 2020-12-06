# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:04:12 2020

@author: Alex
"""
# Import libraries and modules
import pygame, sys, os
import random

# Import individual contribuutions
import utils.alex as FuncAlex
import utils.harri as FuncHarri
import utils.hongyuan as FuncHongyuan
import utils.peggy as FuncPeggy

# Classes and Functions

# Shutdown application
def Shutdown():
    pygame.quit()
    sys.exit()
    os._exit()
    
def CenterWindow():
    FuncAlex.CenterWindow()

# Draw menu buttons - centered on screen (stackable)
def DrawMenuButton(window, width, height, button_number, image):
    return FuncAlex.DrawMenuButton(window, width, height, button_number, image)

# Draw static background - useful for menu screens etc
def DrawStaticBackground(window, width, height, image):
    FuncAlex.DrawStaticBackground(window, width, height, image)
    
# Draw Level Screen    
def DrawLevelScreen(window, width, height, image, level):
    FuncAlex.DrawLevelScreen(window, width, height, image, level)

    
# Draw infinite scroll
def DrawScrollBackground(window, width, speed, image, fps, x):
    return FuncAlex.DrawScrollBackground(window, width, speed, image, fps, x)


#%% Harri's code

""" GLOBAL VAR HARDCODED - REPLACE """
screen_width = 1600
screen_height = 900

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect(center=(screen_width/2,screen_height/2))
        self.life = 1

    def update(self, image):
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect.center = pygame.mouse.get_pos()
        
    def create_rightbullet(self):
        return RightBullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) #return bullet and has the position of wherever the mouse is

    def create_leftbullet(self):
        return LeftBullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) #return bullet and has the position of wherever the mouse is

    def create_downbullet(self):
        return DownBullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) #return bullet and has the position of wherever the mouse is

    def create_upbullet(self):
        return UpBullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) #return bullet and has the position of wherever the mouse is



    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) #return bullet and has the position of wherever the mouse is


class Bullet(pygame.sprite.Sprite):
   def __init__(self,pos_x,pos_y):
       super().__init__()
       self.image = pygame.Surface((50, 10))
       self.image.fill((255,0,0))#colour
       self.rect = self.image.get_rect(center = (pos_x,pos_y))

   def update(self):
       self.rect.x += 10

       if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
           self.kill() #bullet will destroy itself to save memory and improve performance


class Mob(pygame.sprite.Sprite): #spawn enemies
    def __init__(self, image, level):
        self.level = level
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(screen_height - self.rect.height)#spanwns them on x axis outside of screen to the right
        self.rect.x = random.randrange(screen_width + 100, screen_width+500)
        self.speedx = random.randrange(5, 10) * self.level# randomise their speed

    def update(self):
        self.rect.x -= self.speedx #mobs go in left direction
        if self.rect.x <= 0:
            self.rect.y = random.randrange(screen_height - self.rect.height)  # spanwns them on x axis outside of screen to the right
            self.rect.x = random.randrange(screen_width + 100, screen_width + 500)  # spawn in a random place to the right of the screen
            self.speedx = random.randrange(5, 10) * self.level# randomise their speed



#%% Peggy's code
class RightBullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255,0,0))#colour
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.downwards = False

        
    def update(self):
        self.rect.x += 5
        if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
            self.kill() #bullet will destroy itself to save memory and improve performance
            
class LeftBullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255,0,0))#colour
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.downwards = False

        
    def update(self):
        self.rect.x -= 5
        if self.rect.x < 0: #if bullet goes too far to the left,
            self.kill() #bullet will destroy itself to save memory and improve performance
       
        
class DownBullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((10, 50))
        self.image.fill((255,0,0))#colour
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.downwards = False

        
    def update(self):
        self.rect.y += 5
        if self.rect.y >= screen_height + 200: #if bullet goes too far down,
            self.kill() #bullet will destroy itself to save memory and improve performance
       
class UpBullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((10, 50))
        self.image.fill((255,0,0))#colour
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.downwards = False

        
    def update(self):
        self.rect.y -= 5
        if self.rect.x < 0: #if bullet goes too far to up,
            self.kill() #bullet will destroy itself to save memory and improve performance
       
               
            
class Heart(pygame.sprite.Sprite): #spawn enemies
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill((153, 0, 153))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(screen_height - self.rect.height)#spanwns them on x axis outside of screen to the right
        self.rect.x = random.randrange(700, screen_width)
        self.speedx = random.randrange(1, 8)# randomise their speed

    def update(self):
        self.rect.x -= self.speedx #mobs go in left direction
        if self.rect.x <= 0:
            self.rect.y = random.randrange(screen_height - self.rect.height)  # spanwns them on x axis outside of screen to the right
            self.rect.x = random.randrange(700, screen_width)  # spawn in a random place to the right of the screen
            self.speedx = random.randrange(1,8)  # randomise their speed
#currently new mobs dont spanwn, in the futuer after a mob dies, new one will spawn. need to do collision mehcanic first
     
        if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
            self.kill()
            
            
class StarBullet(pygame.sprite.Sprite): #spawn enemies
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(screen_height - self.rect.height)#spanwns them on x axis outside of screen to the right
        self.rect.x = random.randrange(700, screen_width)
        self.speedx = random.randrange(1, 8)# randomise their speed

    def update(self):
        self.rect.x -= self.speedx #mobs go in left direction
        if self.rect.x <= 0:
            self.rect.y = random.randrange(screen_height - self.rect.height)  # spanwns them on x axis outside of screen to the right
            self.rect.x = random.randrange(700, screen_width)  # spawn in a random place to the right of the screen
            self.speedx = random.randrange(1,8)  # randomise their speed
#currently new mobs dont spanwn, in the futuer after a mob dies, new one will spawn. need to do collision mehcanic first
     
        if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
            self.kill()