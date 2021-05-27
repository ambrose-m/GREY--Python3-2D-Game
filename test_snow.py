import snow_class
import unittest
from pygame import Surface

class TestSnow(unittest.TestCase):
    def setUp(self):
        self.snow = snow_class.Snow()
    
    def test_init_image(self):
        self.assertIsInstance(self.snow.image, Surface)

    def test_init_rect(self):
        self.assertEqual(self.snow.rect, (0, 0, 5, 5))
        self.assertEqual(self.snow.rect, self.snow.image.get_rect())

    def test_init_speedx(self):
        self.assertIsInstance(self.snow.speedx, int)  
    
    def test_init_speedy(self):
        self.assertIsInstance(self.snow.speedy, int)  

    def test_update_rect_centerx(self):
        self.snow.update()
        self.assertIsInstance(self.snow.rect.centerx, int)  

    def test_update_rect_centery(self):
        self.snow.update()
        self.assertIsInstance(self.snow.rect.centery, int)  
    

    #Boundary Tests:

    #Tests that speed is within the valid boundary
    def test_boundary_speedx(self):
        self.assertGreaterEqual(self.snow.speedx, -2)
        self.assertLessEqual(self.snow.speedx, 2)    
    
    #Tests that speed is within the valid boundary
    def test_boundary_speedy(self):
        self.assertGreaterEqual(self.snow.speedy, 1)
        self.assertLessEqual(self.snow.speedy, 5)

    #rect.centerx starts at 2. So its valid boundary after adding speedx in update() is 0-4.
    def test_boundary_update_rect_centerx(self):
        self.snow.update()
        self.assertGreaterEqual(self.snow.rect.centerx, 0)
        self.assertLessEqual(self.snow.rect.centerx, 4)

    #rect.centery starts at 2. So its valid boundary after adding speedy in update() is 3-7.
    def test_boundary_update_rect_centery(self):
        self.snow.update()
        self.assertGreaterEqual(self.snow.rect.centery, 3)
        self.assertLessEqual(self.snow.rect.centery, 7)


    #Invalid Value Tests:

    #speedx should be an int. Error will occur in update() during self.rect.centerx += self.speedx
    def test_invalid_speedx(self):
        #if speedx is a string
        self.snow.speedx = 'fail'
        with self.assertRaises(TypeError):
            self.snow.update()

        #if speedx is a tuple
        self.snow.speedx = (5, 5)
        with self.assertRaises(TypeError):
            self.snow.update()

    #speedy should be an int. Error will occur in update() during self.rect.centery += self.speedy
    def test_invalid_speedy(self):
        #if speedy is a string
        self.snow.speedy = 'fail'
        with self.assertRaises(TypeError):
            self.snow.update()
        
        #if speedy is a tuple
        self.snow.speedy = (5, 5)
        with self.assertRaises(TypeError):
            self.snow.update()

if __name__ == '__main__':
	unittest.main()