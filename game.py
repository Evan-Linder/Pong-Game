import pygame
from paddle import Paddle

class Game:
    # game constants (unmutable).
    WIDTH, HEIGHT = 700, 500
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80

    def __init__(self):
        pygame.init()

        # set width and height in a tuple to avoid error and make it unmutable.
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pong game CIS 121")


        #initalize the paddles (10 pixels from the edge, centered vertically)
        self.left_paddle = Paddle(10, self.HEIGHT * 0.5 - self.PADDLE_HEIGHT * 0.5, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        self.right_paddle = Paddle(self.WIDTH - 10 - self.PADDLE_WIDTH, self.HEIGHT * 0.5 - self.PADDLE_HEIGHT * 0.5, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)

    

    def draw_objects(self):
        #set background to red.
        self.win.fill(self.RED)

        for paddle in (self.left_paddle, self.right_paddle):
            paddle.draw_objects(self.win)
            
    def paddle_movement(self, keys):
        # checks left paddle for key presses. (W and S)
        if keys[pygame.K_w] and self.left_paddle.y - self.left_paddle.PADDLE_VELOCITY >= 0:
            self.left_paddle.move(up=True)
        if keys[pygame.K_s] and self.left_paddle.y + self.left_paddle.PADDLE_VELOCITY + self.left_paddle.height <= self.HEIGHT:
            self.left_paddle.move(up=False)

        # checks right paddle for key presses. (Up and down arrows)
        if keys[pygame.K_UP] and self.right_paddle.y - self.right_paddle.PADDLE_VELOCITY >= 0:
            self.right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and self.right_paddle.y + self.right_paddle.PADDLE_VELOCITY + self.right_paddle.height <= self.HEIGHT:
            self.right_paddle.move(up=False)


    def run_game(self):
        # run the game.
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #draw game objects.
            self.draw_objects()

            #define keys and pass it as a paramater to paddle_movement.
            keys = pygame.key.get_pressed()
            self.paddle_movement(keys)
            pygame.display.update()

            # set game fps to 60 so velocity works accordingly (avoids screen tearing).
            clock = pygame.time.Clock()
            clock.tick(60)