import pygame
import json
import os
def save_game(self, filename="/../../saved/save.json"): 
        saved_games_dir = os.path.join(os.getcwd(), 'saved')
        filepath = os.path.join(saved_games_dir, filename)
        if not os.path.exists(saved_games_dir):
            os.makedirs(saved_games_dir)
    
        #the file path
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
        with open(filepath, "w") as file: 
            json.dump(game_state, file, indent=4)
        print(f"Game state saved to {filename}")


def mainscreen():
    from Gameboard import drawing,draw_players,screen,font
    # Main loop

    # Fill the background with white
    screen.fill(255,255,255)
    # Keeping drawing board
    drawing()
    # Update the display
    pygame.display.flip()
