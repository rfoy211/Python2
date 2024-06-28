import pygame

class player:
    def __init__(self, title, size_x, size_y) -> None:
        pygame.init()
        pygame.display.set_caption(title)
        self.canvas = pygame.display.set_mode(size=(size_x, size_y))
        self.clock = pygame.time.clock

    def run(self):
        ball = ball("buoi3/assets/D:\Python2\buoi3\ball.png")
        paddle_1 = ball("buoi3/assets/D:\Python2\buoi3\ball.png")
        paddle_2 = ball("buoi3/assets/D:\Python2\buoi3\ball.png")

        # set up location
        ball.setX(285)
        ball.setY(300)
        paddle_1.setX(0)
        paddle_1.setY(250)
        paddle_2.setX(570)
        paddle_2.setY(250)

        paddle_1.setkeyup("W")
        paddle_1.setkeydown("S")
        paddle_2.setkeyup("Up")
        paddle_2.setkeydown("down")