import pygame
import json
import os
def save_game(self, filename="/../../saved/save.json"): # 调不过来路径,算了
        saved_games_dir = os.path.join(os.getcwd(), 'saved')
        filepath = os.path.join(saved_games_dir, filename)
        if not os.path.exists(saved_games_dir):
            os.makedirs(saved_games_dir)
    
        # 构建完整的文件路径
        filepath = os.path.join(saved_games_dir, filename)
        game_state = {
            "players": [
                {
                    "name": player.name,
                    "money": player.money,
                    "position": player.position,
                    "properties": [(prop.name, prop.price, prop.rent) for prop in player.properties],
                    "jail": player.jail,
                    "jailturns": player.jailturns
                }
                for player in self.players
            ],
            "round_count": self.round_count,
            "turn_count": self.turn_count,
            "current_position": self.current_position
        }
        with open(filepath, "w") as file: # AI filename filepath傻傻分不清 tmd
            json.dump(game_state, file, indent=4)
        print(f"Game state saved to {filename}")


def mainscreen():
    from Gameboard import drawing,draw_players,screen,font
    # Main loop

    # Fill the background with white
    screen.fill(255,255,255)
    # Keeping drawing board
    drawing()
    # draw_players(playerposition)
    # Update the display
    pygame.display.flip()