import pickle 

# save game to a binary file to allow the use of a dictionary.
def save_game_state(game_state, filename):
    with open(filename, "wb") as file: # write as a binary file
        pickle.dump(game_state, file) # write game state to file

def load_game_state(filename):
    try: # attempt to open file 
        with open(filename, "rb") as file: # read as a binary file
            game_state = pickle.load(file) #load game state from file
        return game_state # return the game state.
    except FileNotFoundError:
        return None # return none if file is not found.