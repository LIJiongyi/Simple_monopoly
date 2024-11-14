from Board_back import Boardclass
from monopoly_game_logic import Monopolyclass
import random
import string
from Gameboard import mainscreen
def generate_random_name():
    length = random.randint(1, 20)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#Player management
def Start_gameclass(board_instance: Boardclass, monopoly_game: Monopolyclass):

    while True:  # 无限循环，直到有足够的玩家才退出
        monopoly_game.players = []  # 重置玩家列表，以便重新输入所有玩家
        print("Enter player names (type 'done' when finished):")
    
        while len(monopoly_game.players) < 8: 
            choice = input(f"Do you want to enter a name or generate a random name for Player {len(monopoly_game.players) + 1}? (enter/generate/done): ").strip().lower()
            if choice == 'enter':
                name = input(f"Player {len(monopoly_game.players) + 1}: ").strip()
                if not name:
                    print("Error: No name entered. Please enter a valid name.")
                    continue
                monopoly_game.add_player(name)
                print(f"Added player: {name}")
            elif choice == 'generate':
                name = generate_random_name()
                monopoly_game.add_player(name)
                print(f"Generated name for Player {len(monopoly_game.players)}: {name}")
            elif choice == 'done':
                if len(monopoly_game.players) >= 2:
                    break  # 如果输入'done'且玩家数量足够，退出玩家输入循环
                else:
                    print("Error: Not enough players. Please enter at least 2 players.")
            else:
                print("Invalid choice. Please type 'enter', 'generate', or 'done'.")
                continue

        if len(monopoly_game.players) >= 2:
            mainscreen()
            break  # 玩家数量足够，退出外层循环开始游戏

    while True: 
        monopoly_game.turns()