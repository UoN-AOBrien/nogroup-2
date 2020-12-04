# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:49:02 2020

@author: Peggy
"""
# Import libraries and modules
import pygame


# Import individual contribuutions
import utils.alex as FuncAlex
import utils.harri as FuncHarri
import utils.hongyuan as FuncHongyuan


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
        if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
            self.kill() #bullet will destroy itself to save memory and improve performance
       
        
class DownBullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255,0,0))#colour
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.downwards = False

        
    def update(self):
        self.rect.y += 5
        if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
            self.kill() #bullet will destroy itself to save memory and improve performance
       
class UpBullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255,0,0))#colour
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.downwards = False

        
    def update(self):
        self.rect.y -= 5
        if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
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
    