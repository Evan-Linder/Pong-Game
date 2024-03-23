import pygame

class Ball:
    WHITE = (255, 255, 255)
    MAX_VELOCITY = 4

    def __init__(self, _x, _y, _radius):
        
        # use self.original to reset ball
        self.x = self.original_x = _x
        self.y = self.original_y = _y
        self.radius = _radius
        self.x_velocity = self.MAX_VELOCITY
        self.y_velocity = 0

    #draw the ball on the window.
    def draw_ball(self, win):
        pygame.draw.circle(win, self.WHITE, (self.x, self.y), self.radius)

    #ajust ball velocity
    def move_ball(self):
        
        self.x += self.x_velocity
        self.y += self.y_velocity
    
    #reset the ball to original position and reverse the velocity.
    def reset_ball(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_velocity = 0
        self.x_velocity *= -1




