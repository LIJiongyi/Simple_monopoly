from board import Boardclass
from monopoly import Monopolyclass

#Player management
def Start_gameclass(board_instance: Boardclass, monopoly_game: Monopolyclass):
    # global board_instance 
    # board_instance = board()
    # monopoly_game = Monopoly()

    # adds player up to 8, type 'done' to finish adding more players
    print("Enter player names (max 8 players). Type 'done' when finished:")
    while len(monopoly_game.players) < 8:
        name = input(f"Player {len(monopoly_game.players) + 1}: ")
        while True:
            if name == "done":
                break  # if type done ,quite circle
            elif not name:
                print("Error: No name entered. Please enter a valid name.")
            else:
                monopoly_game.add_player(name)
                print("")
            name = input(f"Player {len(monopoly_game.players) + 1}: ")
        
        # loop until only 1 player is left
        while True: 
            monopoly_game.turns()

        # if len(monopoly_game.players) == 1:
        #     print(f"The game ended! {monopoly_game.players[0].name} wins!")