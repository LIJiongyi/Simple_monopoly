import monopoly_game_logic
from monopoly_game_logic import Monopolyclass
from start_game import Start_gameclass
from Board_back import Boardclass
from Gameboard import mainscreen
import os

def list_saved_games():
    saved_games_dir = os.path.join(os.path.dirname(__file__), 'saved')
    if not os.path.exists(saved_games_dir):
        os.makedirs(saved_games_dir)
    return [f for f in os.listdir(saved_games_dir) if f.endswith('.json')]

if __name__ == "__main__":
    global board_instance 
    board_instance = Boardclass()
    monopoly_game = Monopolyclass()
    print("Welcome to Monopoly!")

    while True:
        choice = input("Type 'new' to start a new game or 'load' to load a saved game: ").strip().lower()
        if choice == 'new':
            Start_gameclass(board_instance, monopoly_game)
            break
        elif choice == 'load':
            saved_games = list_saved_games()
            if not saved_games:
                print("No saved games found. Starting a new game.")
                Start_gameclass(board_instance, monopoly_game)
                break
            print("Saved games:")
            for i, game in enumerate(saved_games):
                print(f"{i + 1}. {game}")
            game_choice = input("Enter the number of the game you want to load: ").strip()
            if game_choice.isdigit() and 1 <= int(game_choice) <= len(saved_games):
                filename = saved_games[int(game_choice) - 1]
                monopoly_game.load_game(filename)
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please type 'new' or 'load'.")