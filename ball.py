import pygame

class Ball:
    WHITE = (255, 255, 255)
    MAX_VELOCITY = 4

    def __init__(self, _x, _y, _radius):
        self.x = self.original_x = _x # x cord
        self.y = self.original_y = _y # y cord
        self.radius = _radius # ball radius
        self.x_velocity = self.MAX_VELOCITY 
        self.y_velocity = 0 

    #draw the ball on the window.
    def draw_ball(self, win):
        pygame.draw.circle(win, self.WHITE, (self.x, self.y), self.radius)

    #adjust the velocity of the ball
    def move_ball(self):
        self.x += self.x_velocity # update x-cord with x-velocity
        self.y += self.y_velocity # update y-cord with y-velocity
    
    #reset the ball to original position and reverse the velocity.
    def reset_ball(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_velocity = 0
        self.x_velocity *= -1




