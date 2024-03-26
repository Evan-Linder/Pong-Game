'''
Abdulaziz Abdirisak, Mustafa Ali, Evan Linder
Pong game
CIS 121 
Movement for left paddle: up(W), down(S)
Movement for right paddle: up(Down Arrow), down(Down Arrow) 
'''

from game import *

if __name__ == "__main__":
    # call a new instance of the game class
    game = Game()

    # Start game loop
    game.run_game()