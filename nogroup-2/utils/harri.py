# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:49:03 2020

@author: Harri
"""
# Import libraries and modules
import pygame, sys, random
# Import individual contribuutions
import utils.alex as FuncAlex
import utils.hongyuan as FuncHongyuan
import utils.peggy as FuncPeggy

class Player(pygame.sprite.Sprite):
    def __init__(self,screen_width, screen_height):
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


class Bullet(pygame.sprite.Sprite):
   def __init__(self,pos_x,pos_y):
       super().__init__()
       self.image = pygame.Surface((50, 10))
       self.image.fill((255,0,0))#colour
       self.rect = self.image.get_rect(center = (pos_x,pos_y))

   def update(self):
       self.rect.x += 10 #bullet speed

       if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
           self.kill() #bullet will destroy itself to save memory and improve performance

            
class Mob(pygame.sprite.Sprite): #spawn enemies
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(screen_height - self.rect.height)#spanwns them on x axis outside of screen to the right
        self.rect.x = random.randrange(screen_width, screen_width + 500)
        self.speedx = random.randrange(3, 8)# randomise their speed

    def update(self):
        self.rect.x -= self.speedx #mobs go in left direction
        if self.rect.x <= 0:
            self.rect.y = random.randrange(screen_height - self.rect.height)  # spanwns them on x axis outside of screen to the right
            self.rect.x = random.randrange(screen_width, screen_width + 500)  # spawn in a random place to the right of the screen
            self.speedx = random.randrange(3, 8)  # randomise their speed

def setup_sprites(screen_width, screen_height):
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.mouse.set_visible(False)  ##hides mouse

    # player group
    player = Player(screen_width, screen_height)
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # bullet group
    bullet_group = pygame.sprite.Group()

    # mob group
    mob = pygame.sprite.Group()
    mob_number = 5
    for i in range(mob_number):  # no of mobs
        m = Mob(screen_width, screen_height)
        mob.add(m)



    return player_group, mob, bullet_group, player, screen

def draw_sprites(player_group, mob,bullet_group,player,screen):
    # check to see if a bullet hits a mob
    hits = pygame.sprite.groupcollide(mob, bullet_group, True,
                                      True)  # bullet needs to run into mob and vice versa so 2 Trues
    for hit in hits:  # this loop adds a mob if a mob dies
        m = Mob()
        mob.add(m)

    # check to see if a mob hits player
    hits = pygame.sprite.spritecollide(player, mob, False)  # hit list if player was hit
    if hits:
        game_running = False  # if player is hit by mob, loop stops and game exits

    mob.update()
    player_group.update()
    mob.draw(screen)
    bullet_group.draw(screen)
    player_group.draw(screen)
    bullet_group.update()

    return player_group, mob,bullet_group
