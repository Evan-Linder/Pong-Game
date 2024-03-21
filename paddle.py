import pygame

class Paddle:
    WHITE = (255,255,255)
    PADDLE_VELOCITY = 6

    def __init__(self, x, y, width, height):
        #set x,y to both self.x,y and self.original_x,y
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw_objects(self, win):
        #draw a rectangle object on the window with specified dimensions.
        pygame.draw.rect(win, self.WHITE, (self.x, self.y, self.width, self.height))


    def move(self, up = True):
        #if up is true adjust paddle velocity to go up (y-cor.), else apply the opposite logic.
        if up:
            self.y -= self.PADDLE_VELOCITY

        else:
            self.y += self.PADDLE_VELOCITY        