import unittest
import coverage
import pygame
import explosion_class

class ExplosionTest(unittest.TestCase):
    def setUp(self):
        self.explosion_sm = explosion_class.Explosion((200, 200), 'sm') 
        self.explosion_lg = explosion_class.Explosion((210, 210), 'lg') 
        self.explosion_xlg = explosion_class.Explosion((220, 220), 'Xlg')  

    #__init__(self, center, size) unit tests:
    def test_init_size(self):    
        self.assertEqual(self.explosion_sm.size, 'sm')  
        self.assertEqual(self.explosion_lg.size, 'lg')
        self.assertEqual(self.explosion_xlg.size, 'Xlg')

    def test_init_image(self):
        self.assertEqual(self.explosion_sm.image, explosion_class.explosion_anim['sm'][0])
        self.assertEqual(self.explosion_lg.image, explosion_class.explosion_anim['lg'][0])
        self.assertEqual(self.explosion_xlg.image, explosion_class.explosion_anim['Xlg'][0])

    def test_init_rect(self):
        self.assertEqual(self.explosion_sm.rect, (184, 184, 32, 32))
        self.assertEqual(self.explosion_lg.rect, (163, 163, 95, 95))
        self.assertEqual(self.explosion_xlg.rect, (115, 115, 210,210))

    def test_init_rectCenter(self):
        self.assertEqual(self.explosion_sm.rect.center, (200, 200)) 
        self.assertEqual(self.explosion_lg.rect.center, (210, 210))  
        self.assertEqual(self.explosion_xlg.rect.center, (220, 220))
        

    def test_init_frame(self):
        self.assertEqual(self.explosion_sm.frame, 0)
        self.assertEqual(self.explosion_lg.frame, 0)
        self.assertEqual(self.explosion_xlg.frame, 0)
    
    def test_init_lastUpdate(self):
        self.assertEqual(self.explosion_sm.last_update, 0) 
        self.assertEqual(self.explosion_lg.last_update, 0) 
        self.assertEqual(self.explosion_xlg.last_update, 0) 
    
    def test_init_framerate(self): 
        self.assertEqual(self.explosion_sm.frame_rate, 50)
        self.assertEqual(self.explosion_lg.frame_rate, 50)
        self.assertEqual(self.explosion_xlg.frame_rate, 50)

    # update(self) unit tests:
    def test_update_lastUpdate(self):
        self.assertEqual(self.explosion_sm.last_update, 0) 
        now = 15000
        self.explosion_sm.update(now)
        self.assertEqual(self.explosion_sm.last_update, now)

    def test_update_frame(self):
        self.assertEqual(self.explosion_sm.frame, 0)
        self.explosion_sm.update(15000)
        self.assertEqual(self.explosion_sm.frame, 1)
        self.explosion_sm.update(20000)
        self.assertEqual(self.explosion_sm.frame, 2)
    
    def test_update_rect(self):
        self.explosion_sm.update(20000)
        self.assertEqual(self.explosion_sm.rect, (184, 184, 32, 32)) 
        self.explosion_lg.update(20000)
        self.assertEqual(self.explosion_lg.rect, (163, 163, 95, 95))
        self.explosion_xlg.update(20000) 
        self.assertEqual(self.explosion_xlg.rect, (115, 115, 210,210))

    def test_update_rectCenter(self):
        self.explosion_sm.update(20000)
        self.assertEqual(self.explosion_sm.rect.center, (200, 200))
    
    def test_update_image(self):
        self.assertEqual(self.explosion_sm.image, explosion_class.explosion_anim['sm'][0])
        self.explosion_sm.update(15000)
        self.assertEqual(self.explosion_sm.image, explosion_class.explosion_anim['sm'][1])
    
    #TO DO: Boundary Tests 
    #center boundaries. not exactly sure what they are but maybe lt 0 and gt ?
    #explosion_anim[self.size][]. size lt 0 and gt ?. second[] index less than 0 and greater than 9
    #self.frame in update(). it's the second [] in exp_anim

    #TO DO: Invalid Value Tests
    # strings and doubles for the center, size, and now variables
             
if __name__ == '__main__':
    unittest.main()