import monopoly_game_logic
from monopoly_game_logic import Monopolyclass
from start_game import Start_gameclass
from Board_back import Boardclass
from Gameboard import mainscreen

if __name__ == "__main__":
    global board_instance 
    board_instance = Boardclass()
    monopoly_game = Monopolyclass()
    print("Welcome to Monopoly!")
    Start_gameclass(board_instance, monopoly_game)
    mainscreen()
    