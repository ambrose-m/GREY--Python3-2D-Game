import unittest
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,hp):
        super().__init__()
        self.image = pygame.image.load('./images/jet.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.radius = (self.rect.centerx - self.rect.x)
        self.hp = hp
        self.speed = 10
        self.shoot_delay = 100
        self.last_shot = pygame.time.get_ticks()
        self.machinegun = False
        
    def update(self):
        key = pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        
        self.rect.centerx=mouse_pos[0]
        self.rect.centery=mouse_pos[1]

        if self.machinegun:
            if key[0] == 1:
                if pygame.time.get_ticks() - self.last_shot > self.shoot_delay:
                    if not muted:
                        gunshot.play()
                    self.last_shot = pygame.time.get_ticks()
                    bullet=Bullet(-1,50,'jet')
                    bullet.rect.centerx=player.rect.centerx
                    bullet.rect.centery=player.rect.centery
                    all_sprites.add(bullet)
                    all_bullets.add(bullet)


pygame.display.init()
pygame.display.set_mode((800, 600))

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)

upgrade_anim = []
for i in range(1,10):
    filename = './images/Picture{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(black)
    img = pygame.transform.scale(img,(135,135))
    upgrade_anim.append(img)
player = Player(6)


class Upgrade_anim(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.image = upgrade_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        self.rect.center = player.rect.center
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame +=1
            if self.frame == len(upgrade_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = upgrade_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class TestUpgradeAnim(unittest.TestCase):

	def testNewObjectGivenValidCenter(self):
		expected = (25, 25)
		actual = Upgrade_anim(expected)
		self.assertEqual(actual.rect.center, expected)
		self.assertEqual(actual.frame, 0)

	def testNewObjectGivenNegativeCenter(self):
		expected = (-1, -1)
		actual = Upgrade_anim(expected)
		self.assertEqual(actual.rect.center, expected)

	def testUpdateGivenKill(self):
		actual = Upgrade_anim((25, 25))
		actual.frame = 9
		actual.update()
		self.assertFalse(actual.alive())


if __name__ == '__main__':
	unittest.main()

