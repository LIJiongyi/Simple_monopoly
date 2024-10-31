from board import Boardclass
from monopoly import Monopolyclass

#Player management
def Start_gameclass(board_instance: Boardclass, monopoly_game: Monopolyclass):
    # global board_instance 
    # board_instance = board()
    # monopoly_game = Monopoly()

    # adds player up to 8, type 'done' to finish adding more players
    # print("Enter player names (max 8 players). Type 'done' when finished:")

    while True:  # 无限循环，直到有足够的玩家才退出
        monopoly_game.players = []  # 重置玩家列表，以便重新输入所有玩家
        print("Enter player names (type 'done' when finished):")
    
        while len(monopoly_game.players) < 8:
            name = input(f"Player {len(monopoly_game.players) + 1}: ").strip()
        
            if name.lower() == "done":
                break  # 如果输入'done'，退出玩家输入循环
            elif not name:
                print("Error: No name entered. Please enter a valid name.")
            else:
                monopoly_game.add_player(name)
                print(f"Added player: {name}")
    
        if len(monopoly_game.players) < 2:
            print("Error: Not enough players. Please enter at least 2 players.")
        else:
            break  # 玩家数量足够，退出外层循环开始游戏

    while True: 
        monopoly_game.turns()

        # if len(monopoly_game.players) == 1:
        #     print(f"The game ended! {monopoly_game.players[0].name} wins!")