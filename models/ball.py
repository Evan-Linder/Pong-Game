import pygame, random

class Ball:
    WHITE = (255, 255, 255)
    MAX_VELOCITY = 4

    def __init__(self, _x, _y, _radius):
        self.x = self.original_x = _x # x cord
        self.y = self.original_y = _y # y cord
        self.radius = _radius # ball radius
        self.x_velocity = random.choice([-self.MAX_VELOCITY, self.MAX_VELOCITY]) # randomize the x velocity of the ball on start
        self.y_velocity = 0 # set to 0 for testing purposes
        
        # This will randomize the y velocity of the ball, commented out for testing purposes
        '''self.y_velocity = random.choice([-self.MAX_VELOCITY, self.MAX_VELOCITY]) '''

    
    def draw_ball(self, win):
        pygame.draw.circle(win, self.WHITE, (self.x, self.y), self.radius) # draw the ball on the window.

    
    def move_ball(self):
        self.x += self.x_velocity # update x-cord with x-velocity
        self.y += self.y_velocity # update y-cord with y-velocity
    
    
    def reset_ball(self):
        self.x = self.original_x # set x cord to its defaulted value
        self.y = self.original_y # set y cord to its defaulted value
        self.y_velocity = 0 # set to 0 for testing purposes
        self.x_velocity =  random.choice([-self.MAX_VELOCITY, self.MAX_VELOCITY]) # randomize x velocity

        # commented out for tesing purposes
        '''self.y_velocity = random.choice([-self.MAX_VELOCITY, self.MAX_VELOCITY])'''






