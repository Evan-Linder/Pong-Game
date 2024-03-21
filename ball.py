import pygame

class Ball:
    WHITE = (255, 255, 255)

    def __init__(self, _x, _y, _radius):
        
        # use self.original to reset ball
        self.x = self.original_x = _x
        self.y = self.original_y = _y
        self.radius = _radius

    #draw the ball on the window.
    def draw_ball(self, win):
        pygame.draw.circle(win, self.WHITE, (self.x, self.y), self.radius)


