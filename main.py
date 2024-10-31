import Monopoly
from Monopoly import Monopoly, board, Start_game


if __name__ == "__main__":
    global board_instance 
    board_instance = board()
    monopoly_game = Monopoly()
    Start_game(board_instance, monopoly_game)