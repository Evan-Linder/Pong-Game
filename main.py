'''
Abdulaziz Abdirisak, Evan Linder
Pong game
CIS 121 

***Instructions***

Movement for left paddle: up (W), down (S)
Movement for right paddle: up (Up Arrow), down (Down Arrow) 

First to 5 wins, you can change the max score within the game.py file 
for testing purposes if you wish. 

Closing the game using the close button ("X"), will 
create a saved_game.txt file. Upon reopening the game, 
you will be prompted to load the saved game file. If you chose 
not to load the game file, it will create a fresh game. After 
the max score is reached and the winner is displayed, the saved game
file will be deleted.
'''

from game import *

if __name__ == "__main__":
    # call a new instance of the game class
    game = Game()

    # Start game loop
    game.run_game()