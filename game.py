import pygame
from paddle import *
from ball import *

class Game:
    # game constants (unmutable).
    WIDTH, HEIGHT = 700, 500
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PADDLE_WIDTH, PADDLE_HEIGHT = 10, 90
    BALL_RADIUS = 7
    MAX_SCORE = 1

    def __init__(self):
        pygame.init()

        # set width and height in a tuple to avoid error and make it unmutable.
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pong game-CIS 121")

        #create game text font
        self.font = pygame.font.SysFont(None, 36)

        # returns true or flase dpending on user input
        self.load_game_prompt()

        #set scores to 0
        self.left_score = 0
        self.right_score = 0

        #initalize the paddles (10 pixels from the edge, centered vertically)
        self.left_paddle = Paddle(10, self.HEIGHT * 0.5 - self.PADDLE_HEIGHT * 0.5, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        self.right_paddle = Paddle(self.WIDTH - 10 - self.PADDLE_WIDTH, self.HEIGHT * 0.5 - self.PADDLE_HEIGHT * 0.5, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)

        #initalize the ball (centered vertically and horizontally).
        self.ball = Ball(self.WIDTH * 0.5, self.HEIGHT * 0.5, self.BALL_RADIUS)
        
    def load_game_prompt(self):
        load_game_text = self.font.render("Do you want to load your preview game? (Y/N)", True, self.WHITE) # create load game prompt text
        self.win.fill(self.RED) # fill the background red
        self.win.blit(load_game_text,(self.WIDTH * 0.5 - load_game_text.get_width() * 0.5, self.HEIGHT * 0.5 - load_game_text.get_height()* 0.5)) # display text, centered vertically and horizontally realtive to the text height and width
        pygame.display.update() # update the display
        
         
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: # check for key presses
                    if event.key == pygame.K_y: 
                        return True # load saved game
                    elif event.key == pygame.K_n: 
                        return False # load new game
    
    def save_game(self, filename):
        # save the current game state to a dictionary 
        game_state = {
            "left_score": self.left_score,
            "right_score": self.right_score,
            "left_paddle": self.left_paddle,
            "right_paddle": self.right_paddle,
            "ball": self.ball
        }
        




    
    def draw_objects(self):

        #set background to red.
        self.win.fill(self.RED)


        for paddle in (self.left_paddle, self.right_paddle): # loop over each paddle.
            paddle.draw_paddles(self.win) #Draw each paddle on the game window.

        # draw and position the left scoring text
        left_score_text = self.font.render(f'P1: {self.left_score}', 1, self.WHITE) # create scoring text
        self.win.blit(left_score_text, (self.WIDTH * 0.25 - left_score_text.get_width() * 0.5, 20)) # display scoring text
        
        #draw and position the right scoring text
        right_score_text = self.font.render(f'P2: {self.right_score}', 1, self.WHITE)
        self.win.blit(right_score_text, (self.WIDTH * 0.75 - right_score_text.get_width() * 0.75, 20))

        
        # draw ball
        self.ball.draw_ball(self.win)
            
    def paddle_movement(self, keys):
        # checks left paddle for key presses. (W and S)
        if keys[pygame.K_w] and self.left_paddle.y - self.left_paddle.PADDLE_VELOCITY >= 0: # ensure the paddle stays within the top edge
            self.left_paddle.move(up=True) # Move the left paddle upwards.
        if keys[pygame.K_s] and self.left_paddle.y + self.left_paddle.PADDLE_VELOCITY + self.left_paddle.height <= self.HEIGHT: #ensure the paddle stays within the bottom edge
            self.left_paddle.move(up=False) # Move the left paddle downwards.

        # checks right paddle for key presses. (Up and down arrows)
        if keys[pygame.K_UP] and self.right_paddle.y - self.right_paddle.PADDLE_VELOCITY >= 0:
            self.right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and self.right_paddle.y + self.right_paddle.PADDLE_VELOCITY + self.right_paddle.height <= self.HEIGHT:
            self.right_paddle.move(up=False)

    def collision(self):
        # Check if the ball has collided with the top or bottom edge, if so, reverse the x-velocity.
        if self.ball.y + self.ball.radius >= self.HEIGHT: # check if ball hit the top edge
            self.ball.y_velocity *= -1 # reverse y-velocity
        elif self.ball.y - self.ball.radius <= 0: # check if the ball hit the bottom edge
            self.ball.y_velocity *= -1 # reverse y-velocity

        # Check for paddle collisons
        if self.ball.x_velocity < 0: # check if the ball is moving left
            if self.ball.y >= self.left_paddle.y and self.ball.y <= self.left_paddle.y + self.left_paddle.height: # check if the ball is within range of the paddle
                 if self.ball.x - self.ball.radius <= self.left_paddle.x + self.left_paddle.width: # check for collision 
                    self.ball.x_velocity *= -1 # reverse the x-velocity
        
                    # calculate how far the ball is from the middle of the paddle on collision.
                    middle_y = self.left_paddle.y + self.left_paddle.height * 0.5 # find paddles middle.
                    difference_in_y = middle_y - self.ball.y #find y-cord difference
                    reduction_factor = (self.left_paddle.height * 0.5) / self.ball.MAX_VELOCITY #scale difference
                    y_velocity = difference_in_y / reduction_factor # match balls y-velocity
                    self.ball.y_velocity = -1 * y_velocity #reverse balls y-velocity
        
        # run the same collison check for the right paddle.
        else:
            if self.ball.y >= self.right_paddle.y and self.ball.y <= self.right_paddle.y + self.right_paddle.height:
                if self.ball.x + self.ball.radius >= self.right_paddle.x:
                    self.ball.x_velocity *= -1
                    
                    middle_y = self.right_paddle.y + self.left_paddle.height * 0.5 
                    difference_in_y = middle_y - self.ball.y 
                    reduction_factor = (self.right_paddle.height * 0.5) / self.ball.MAX_VELOCITY 
                    y_velocity = difference_in_y / reduction_factor
                    self.ball.y_velocity = -1 * y_velocity 
    
    
    def display_winner(self, winner_result):
        winner_text = self.font.render(f'{winner_result}', 1, self.WHITE) # set result as the winner text.
        winner_text_rect = winner_text.get_rect(center = (self.WIDTH * 0.5, self.HEIGHT * 0.5)) # enclose text in a rect, centered vertically and horizontally
        self.win.fill(self.RED)
        self.win.blit(winner_text, winner_text_rect) # display winner 


    def run_game(self):
    
        # create start window text.
        start_text = self.font.render("Click to start the game.", True, self.WHITE) # create starting text
        self.win.fill(self.RED) # fill window  background red.
        self.win.blit(start_text, (self.WIDTH * 0.5 - start_text.get_width() * 0.5, self.HEIGHT * 0.5 - start_text.get_height() * 0.5)) # center vertically and horizontally
        pygame.display.update() # update display

        # wait for user click
        waiting_for_click = True
        while waiting_for_click: # while waiting for click display start text
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # check if user clicks the close button.
                    waiting_for_click = False 
                    pygame.quit # close the window
                
                elif event.type == pygame.MOUSEBUTTONDOWN: # check if user clicks mouse button
                    waiting_for_click = False # break the loop and run the game.

        # run the game.
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False # break the game loop

            #draw game objects.
            self.draw_objects()

            #ball movement/reset if the ball goes out of bounds (left or right). 
            self.ball.move_ball()

            if self.ball.x < 0: # check if the ball has gone out of bounds (left)
                self.left_score += 1 # increment score

                if self.left_score >= self.MAX_SCORE: # check if max score is reached.
                    self.display_winner("Player 1 is the winner!") # send parameter to display winner
                    
                
                else:
                    self.ball.reset_ball() # reset ball to orgin
                
            elif self.ball.x > self.WIDTH: # check if the ball has gone out of bounds (right)
                self.right_score += 1

                if self.right_score >= self.MAX_SCORE:
                    self.display_winner("Player 2 is the winner!")
                
                else:
                    self.ball.reset_ball()

            #define keys and pass it as a paramater to paddle_movement.
            keys = pygame.key.get_pressed()
            self.paddle_movement(keys)
            pygame.display.update()

            # set game fps to 60 so velocity works accordingly (avoids screen tearing).
            clock = pygame.time.Clock()
            clock.tick(60)

            self.collision()

