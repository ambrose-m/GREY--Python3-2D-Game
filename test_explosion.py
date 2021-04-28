import unittest
import coverage
import pygame
import ExplosionClass

class ExplosionTest(unittest.TestCase):
    #__init__(self, center, size) unit tests:
    def test_init_size(self):   
        exp1 = ExplosionClass.ExplosionClass((205, 220), 'sm')   
        self.assertEqual(exp1.size, 'sm')
        exp2 = ExplosionClass.ExplosionClass((205, 220), 'lg')     
        self.assertEqual(exp2.size, 'lg')
        exp3 = ExplosionClass.ExplosionClass((205, 220), 'Xlg')    
        self.assertEqual(exp3.size, 'Xlg')

    def test_init_image(self):
        exp1 = ExplosionClass.ExplosionClass((200, 120), 'sm') 
        self.assertEqual(exp1.image, ExplosionClass.explosion_anim['sm'][0])
        exp2 = ExplosionClass.ExplosionClass((205, 220), 'lg')  
        self.assertEqual(exp2.image, ExplosionClass.explosion_anim['lg'][0])
        exp3 = ExplosionClass.ExplosionClass((205, 220), 'Xlg')   
        self.assertEqual(exp3.image, ExplosionClass.explosion_anim['Xlg'][0])

    def test_init_rect(self):
        exp1 = ExplosionClass.ExplosionClass((205, 220), 'sm') 
        self.assertEqual(exp1.rect, (189, 204, 32, 32))
        exp2 = ExplosionClass.ExplosionClass((205, 220), 'lg')  
        self.assertEqual(exp2.rect, (158, 173, 95, 95))
        exp3 = ExplosionClass.ExplosionClass((205, 220), 'Xlg')   
        self.assertEqual(exp3.rect, (100, 115, 210,210))

    def test_init_rectCenter(self):
        exp1 = ExplosionClass.ExplosionClass((205, 220), 'sm') 
        self.assertEqual(exp1.rect.center, (205, 220))
        exp2 = ExplosionClass.ExplosionClass((200, 200), 'lg')  
        self.assertEqual(exp2.rect.center, (200, 200))
        exp3 = ExplosionClass.ExplosionClass((195, 230), 'Xlg')   
        self.assertEqual(exp3.rect.center, (195, 230))
        

    def test_init_frame(self):
        exp = ExplosionClass.ExplosionClass((205, 220), 'lg')  
        self.assertEqual(exp.frame, 0)
    
    def test_init_lastUpdate(self):
        exp = ExplosionClass.ExplosionClass((205, 220), 'Xlg') 
        self.assertEqual(exp.last_update, 0) 
    
    def test_init_framerate(self):
        exp = ExplosionClass.ExplosionClass((205, 220), 'lg')  
        self.assertEqual(exp.frame_rate, 50)

    # update(self) unit tests:
    def test_update_lastUpdate(self):
        exp = ExplosionClass.ExplosionClass((205, 220), 'lg') 
        self.assertEqual(exp.last_update, 0) 
        now = 15000
        exp.update(now)
        self.assertEqual(exp.last_update, now)

    def test_update_frame(self):
        exp = ExplosionClass.ExplosionClass((205, 220), 'sm') 
        self.assertEqual(exp.frame, 0)
        exp.update(15000)
        self.assertEqual(exp.frame, 1)
        exp.update(20000)
        self.assertEqual(exp.frame, 2)
    
    def test_update_rect(self):
        exp1 = ExplosionClass.ExplosionClass((205, 220), 'sm') 
        exp1.update(20000)
        self.assertEqual(exp1.rect, (189, 204, 32, 32))
        exp2 = ExplosionClass.ExplosionClass((205, 220), 'lg')  
        exp2.update(20000)
        self.assertEqual(exp2.rect, (158, 173, 95, 95))
        exp3 = ExplosionClass.ExplosionClass((205, 220), 'Xlg')  
        exp3.update(20000) 
        self.assertEqual(exp3.rect, (100, 115, 210,210))

    def test_update_rectCenter(self):
        exp = ExplosionClass.ExplosionClass((195, 180), 'sm') 
        exp.update(20000)
        self.assertEqual(exp.rect.center, (195, 180))
    
    def test_update_image(self):
        exp = ExplosionClass.ExplosionClass((205, 220), 'sm') 
        self.assertEqual(exp.image, ExplosionClass.explosion_anim['sm'][0])
        exp.update(15000)
        self.assertEqual(exp.image, ExplosionClass.explosion_anim['sm'][1])
             
if __name__ == '__main__':
    unittest.main()