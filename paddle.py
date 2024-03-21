import pygame

class Paddle:
    WHITE = (255,255,255)
    PADDLE_VELOCITY = 6

    def __init__(self, _x, _y, _width, _height):
        #set x,y to both self.x,y and self.original_x,y (use original to reset paddles).
        self.x = self.original_x = _x
        self.y = self.original_y = _y
        self.width = _width
        self.height = _height

    #draw paddles on the window.
    def draw_paddles(self, win):
        pygame.draw.rect(win, self.WHITE, (self.x, self.y, self.width, self.height))


    def move(self, up = True):
        #if up is true adjust paddle velocity to go up (y-coor.), else apply the opposite logic.
        if up:
            self.y -= self.PADDLE_VELOCITY

        else:
            self.y += self.PADDLE_VELOCITY        