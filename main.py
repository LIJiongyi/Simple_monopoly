import monopoly
from monopoly import Monopolyclass
from start_game import Start_gameclass
from board import Boardclass

if __name__ == "__main__":
    global board_instance 
    board_instance = Boardclass()
    monopoly_game = Monopolyclass()
    Start_gameclass(board_instance, monopoly_game)