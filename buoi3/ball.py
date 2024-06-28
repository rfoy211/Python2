import pygame

class ball:
    def __init__(self, img_url, speed_x, speed_y) -> None:
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.img_url = pygame.image.load(img_url)

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
    
    def move(self, paddle_x, paddle_y, paddle_distance):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= (paddle_x + paddle_distance) and paddle_y <= self.y <=(paddle_y+120):
            self.speed_x *= -1

        if self.x <= 0 or self.x >= 570:
            self.speed_x = -self.speed_x
        if self.y <= 0 or self.y >= 570:
            self.speed_y = -self.speed_y
