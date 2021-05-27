import pygame
import random

screen_w=1366
screen_h=768
pygame.display.init()
pygame.display.set_mode((800, 600))

class Snow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/snow.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speedy = random.randrange(1,5)
        self.speedx = random.randrange(-2,2)
        
    def update(self):
        self.rect.centery += self.speedy
        self.rect.centerx += self.speedx
        if self.rect.right>screen_w or self.rect.left<0 or self.rect.bottom>screen_h:
            self.kill()
            