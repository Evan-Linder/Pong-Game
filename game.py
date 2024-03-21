import pygame
from paddle import Paddle

class Game:
    #create game constants (unmutable).
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



    def run(self):
        #update the display
        pygame.display.update()




    def run_game(self):
        # run the game.
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #draw game objects.
            self.draw_objects()
            pygame.display.update()

