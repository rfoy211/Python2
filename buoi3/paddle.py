import pygame
class Paddle:
    def __init__(self, img_url) -> None:
        self.img = pygame.image.load(img_url)

    # set location
    def setX(self, x):
        self.x = x

    def setX(self, y):
        self.y = y

    # get location
    def getX(self):
        return self.x
    
    def getX(self):
        return self.y
    # set key press
    
    def setkeyup(self, key_up):
        self.key_up = key_up

    def setkeydown(self, key_down):
        self.key_down = key_down

    def getkeyup(self):
        return self.key_up
    
    def getkeydown(self):
        return self.key_down
    
    def move(self, key_press):
        match key_press:
            
