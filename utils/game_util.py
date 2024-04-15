import pickle
import os

# save game to a binary file to allow the use of a dictionary.
def save_game_state(game_state, filename):
    custom_file_path = os.path.join("utils", filename) # save the game state to the utils folder.
    with open(custom_file_path, "wb") as file: # write as a binary file
        pickle.dump(game_state, file) # write game state to file

def load_game_state(filename):
    try: # attempt to open file 
        with open(filename, "rb") as file: # read as a binary file
            game_state = pickle.load(file) #load game state from file
        return game_state # return the game state.
    except FileNotFoundError:
        return None # return none if file is not found.

class PauseState:
    def __init__(self):
        self.paused = False 

    def toggle_pause(self):
        self.paused = not self.paused # toggle pause state (false => true and true => false)

    def is_paused(self):
        return self.paused # return pause state.
    

