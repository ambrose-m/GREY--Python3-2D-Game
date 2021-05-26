import pygame

pygame.display.init()
pygame.display.set_mode((800, 600))

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['Xlg'] = []

for i in range(9):
    filename = './images/regularExplosion0{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(black)
    img_Xlg = pygame.transform.scale(img, (210,210))
    explosion_anim['Xlg'].append(img_Xlg)
    img_lg = pygame.transform.scale(img, (95, 95))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    #Added 'now' as a parameter to help with testing. 
    #Original code commented out.
    def update(self, now):
        #now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center