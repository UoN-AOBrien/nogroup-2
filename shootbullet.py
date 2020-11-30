import pygame, sys

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
#

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


# General setup
pygame.init()
clock = pygame.time.Clock()
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
mob = pygame.sprite.Group()
mob_number = 5
for i in range(mob_number):#no of mobs
    m = Mob()
    mob.add(m)
    #player.add(m)#might take this out

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #when you click the mouse
            bullet_group.add(player.create_bullet())

    screen.fill((30,30,30))
    mob.update()
    player_group.update()
    mob.draw(screen)
    bullet_group.draw(screen)
    player_group.draw(screen)
    bullet_group.update()
    pygame.display.flip()
    clock.tick(120)

#rectangles require more work and maintennce
