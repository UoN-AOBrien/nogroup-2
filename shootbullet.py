import pygame, sys, random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))#50pixels wide and high
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
        self.rect.x += 5

        if self.rect.x >= screen_width + 200: #if bullet goes too far to the right,
            self.kill() #bullet will destroy itself to save memory and improve performance
           
class Mob(pygame.sprite.Sprite): #spawn enemies
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(screen_height - self.rect.height)#spanwns them on x axis outside of screen to the right
        self.rect.x = random.randrange(700, screen_width)
        self.speedx = random.randrange(1, 8)# randomise their speed

    def update(self):
        self.rect.x -= self.speedx #mobs go in left direction
        if self.rect.x <= 0:
            self.rect.y = random.randrange(screen_height - self.rect.height)  # spanwns them on x axis outside of screen to the right
            self.rect.x = random.randrange(700, screen_width)  # spawn in a random place to the right of the screen
            self.speedx = random.randrange(1, 8)  # randomise their speed
#currently new mobs dont spanwn, in the futuer after a mob dies, new one will spawn. need to do collision mehcanic first

class Boss(pygame.sprite.Sprite): #spawn enemies
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.y = (screen_height//2)#spanwns them on x axis outside of screen to the right
        self.rect.x = screen_width - 25
        self.speedy = 4

    def update(self):
        self.rect.y += self.speedy #mobs go in left direction

        if self.rect.y == 0 or self.rect.y == screen_height:
            self.speedy = self.speedy * -1 #changes direction of y speed

    def create_boss_bullet(self):
        return Boss_Bullet(boss.rect.x, boss.rect.y) #

class Boss_Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255,0,0))#colour
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

    def update(self):
        self.rect.x -= 5 #shoots along x axis left

        if self.rect.x < -100: #if bullet goes too far to the left
            self.kill() #bullet will destroy itself to save memory and improve performance


# General setup
pygame.init()

# game screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.mouse.set_visible(False) ##hides mouse

#player group
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

#bullet group
bullet_group = pygame.sprite.Group()

#mob group
#mob = pygame.sprite.Group()
#mob_number = 1
#for i in range(mob_number):#no of mobs
 #   m = Mob()
  #  mob.add(m)

#boss bulletgroup
boss_bullet_group = pygame.sprite.Group()

#boss group
boss = Boss()
boss_group = pygame.sprite.Group()
boss_group.add(boss)
time_elapsed = 0
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #when you click the mouse
            bullet_group.add(player.create_bullet())

     #check to see if a bullet hits a mob
 #   hits = pygame.sprite.groupcollide(mob, bullet_group, True, True)#bullet needs to run into mob and vice versa so 2 Trues
 #   for hit in hits: #this loop adds a mob if a mob dies
  #      m = Mob()
  #      mob.add(m)

    #check to see if a mob hits player
   # hits = pygame.sprite.spritecollide(player, mob, False) #hit list if player was hit
   # if hits:
    #    running = False #if player is hit by mob, loop stops and game exits

    hits = pygame.sprite.groupcollide(boss_group, bullet_group, True, True)

    screen.fill((30,30,30))
    dt = clock.tick() #dt measure in ms, 250ms = 0.25s
    time_elapsed += dt
    if time_elapsed > 10:
        boss_bullet_group.add(boss.create_boss_bullet())
        time_elapsed = 0


    #mob.update()
    player_group.update()
    #mob.draw(screen)
    boss_bullet_group.update()
    boss_group.update()
    boss_bullet_group.draw(screen)
    boss_group.draw(screen)
    bullet_group.draw(screen)
    player_group.draw(screen)
    bullet_group.update()
    pygame.display.flip()
    clock.tick(120)

