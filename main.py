'''
Abdulaziz Abdirisak, Evan Linder
Pong game
CIS 121 

***Instructions***

Movement for left paddle: up (W), down (S)
Movement for right paddle: up (Up Arrow), down (Down Arrow) 

First to 3 wins, you can change the max score within the game.py file 
for testing purposes if you wish. Also, within the models/ball file, I commented 
out the code that randomizes the y velocity of the models/ball on game starts and ball resets 
for easier testing.

Spacebar will pause and unpause the game.

Closing the game using the close button ("X") during a current game will 
create a saved_game.txt file (saved to the utils folder). Upon reopening the game, 
you will be prompted to load the saved game file. If you chose not to load 
the game file, it will initalize a fresh game and delete the saved file. After
the max score is reached the winner is displayed. If there is a saved game file 
it will be deleted.
'''

from game import *

if __name__ == "__main__":
    # call a new instance of the game class
    game = Game()

    # Start game loop
    game.run_game()