import pygame
import pygame.locals
import unittest

pygame.init()
screen_w=1366
screen_h=768
screen=pygame.display.set_mode([screen_w,screen_h],pygame.HIDDEN)
muted = False
all_sprites=pygame.sprite.Group()
all_bullets=pygame.sprite.Group()
gunshot = pygame.mixer.Sound('./audio/gunshot.wav')
gunshot.set_volume(.2)
mousePress = (True, True, True)

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
        
    # add key parameter to simulate a mouse key being pressed
    # timing if statement removed for testing
    def update(self, key):
        # key = pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        
        self.rect.centerx=mouse_pos[0]
        self.rect.centery=mouse_pos[1]

        if self.machinegun:
            if key[0] == 1:
                # if pygame.time.get_ticks() - self.last_shot > self.shoot_delay:
                if not muted:
                    gunshot.play()
                self.last_shot = pygame.time.get_ticks()
                bullet=Bullet(-1,50,'jet')
                bullet.rect.centerx=player.rect.centerx
                bullet.rect.centery=player.rect.centery
                all_sprites.add(bullet)
                all_bullets.add(bullet)


# needed in order to test Player class
class Bullet(pygame.sprite.Sprite):
    def __init__(self,direction,speed,btype):
        super().__init__()
        self.type = btype
        if self.type == 'jet':
            if player.machinegun:
                self.image = pygame.image.load('./images/bullet2.png').convert_alpha()
            else:
                self.image=pygame.image.load('./images/bullet.png').convert_alpha()
        if self.type == 'ejet':
            self.image = pygame.image.load('./images/ebullet.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.direction = direction
        self.speed = speed


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.playerHealth = 100
        self.player = Player(self.playerHealth)

    def tearDown(self):
        self.player = None

    def test_init_health(self):
        self.assertEqual(self.player.hp, self.playerHealth)

    def test_init_speed(self):
        self.assertEqual(self.player.speed, 10)
    
    def test_init_machine_gun(self):
        self.assertEqual(self.player.machinegun, False)

    def test_init_shoot_delay(self):
        self.assertEqual(self.player.shoot_delay, 100)

    def test_update_no_machine_gun_no_bullet_added(self):
        numBullets = len(all_bullets)
        self.player.update(mousePress)
        newNumBullets = len(all_bullets)
        self.assertEqual(numBullets, newNumBullets)

    def test_update_with_machine_gun_bullet_added_to_bullets(self):
        self.player.machinegun = True
        numBullets = len(all_bullets)
        self.player.update(mousePress)
        newNumBullets = len(all_bullets)
        self.assertEqual(numBullets + 1, newNumBullets)

    def test_update_with_machine_gun_bullet_added_to_sprites(self):
        self.player.machinegun = True
        numSprites = len(all_sprites)
        self.player.update(mousePress)
        newNumSprites = len(all_sprites)
        self.assertEqual(numSprites + 1, newNumSprites)


player=Player(6)
all_sprites.add(player)
if __name__=='__main__':
    # player=Player(6)
    # all_sprites.add(player)
    unittest.main()



# Trying to simulate mouse click:
    # newevent = pygame.event.Event(pygame.locals.MOUSEBUTTONDOWN, mod=pygame.locals.KMOD_NONE)
    # pygame.event.post(newevent)
    # newevent = pygame.event.Event(pygame.locals.MOUSEBUTTONUP, mod=pygame.locals.KMOD_NONE)
    # pygame.event.post(newevent)
    # for event in pygame.event.get():
    #     if event.type == pygame.MOUSEBUTTONDOWN: 
    #         print("Click!")
    # self.player.update()