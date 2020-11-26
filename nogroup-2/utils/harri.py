# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:49:03 2020

@author: Harri
"""
# Import libraries and modules
import pygame, sys
# Import individual contribuutions
import utils.alex as FuncAlex
import utils.hongyuan as FuncHongyuan
import utils.peggy as FuncPeggy

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,100))#100pixels wide and high
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center=(screen_width/2,screen_height/2))


    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) #return bullet and has the position of wherever the mouse is


class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255,0,0))#colour
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

    def update(self):
        self.rect.x += 5 #bullet speed

        if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
            self.kill() #bullet will destroy itself to save memory and improve performance
           

   
      
