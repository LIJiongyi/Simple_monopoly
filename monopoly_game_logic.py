import random
from Player import Playerclass
from Board_back import Boardclass, Property_Slot, Chance_Slot, Gotojail_Slot,Goslot,Tax_Slot,Free_Parking_Slot, Visiting_Slot  # note that the first word can also be uppercase, it is a OS system(Windows,Unix)
import sys
from Gameboard import mainscreen
import json
# Game Logic
class Monopolyclass:
    def save_game_state(self, filename):
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
        with open(filename, "w") as file:
            json.dump(game_state, file, indent=4)
        print(f"Game state saved to {filename}")

    def load_game(self, filename="game_state.json"):
        with open(filename, "r") as file:
            game_state = json.load(file)
        
        self.players = []
        for player_data in game_state["players"]:
            player = Playerclass(player_data["name"], self.board)
            player.money = player_data["money"]
            player.position = player_data["position"]
            player.jail = player_data["jail"]
            player.jailturns = player_data["jailturns"]
            player.properties = [Property(name, price, rent) for name, price, rent in player_data["properties"]]
            self.players.append(player)
        
        self.round_count = game_state["round_count"]
        self.turn_count = game_state["turn_count"]
        self.current_position = game_state["current_position"]
        print(f"Game state loaded from {filename}")
 
    def __init__(self):
        self.players = []
        self.round_count = 0  # count round
        self.turn_count = 0
        self.current_position = 0
        self.board = Boardclass()
        
    # Add players
    def add_player(self, name):
        self.players.append(Playerclass(name, self.board))

    # Roll dices
    def roll_dice(self):
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        return self.dice1,self.dice2


    #button function
    def button(self,screen,font):
        self.button_width=200
        self.button_height=50
        self.button_x = (screen.get_width() // 2) - (self.button_width // 2)
        self.button_y = screen.get_height() - 200  # 按钮位置靠近底部

        # 存储按钮矩形用于检测点击
        self.roll_dice_button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        pygame.draw.rect(screen, (0, 255, 0), self.roll_dice_button_rect)

        text_surface = font.render("Roll Dice", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.roll_dice_button_rect.center)
        screen.blit(text_surface, text_rect)

    def if_botton_clicked(self, mouse_pos):
        if hasattr(self, 'roll_dice_button_rect') and self.roll_dice_button_rect.collidepoint(mouse_pos):
            return True
        return False

    # player roll 2 dices and move accordin to the sum of both dices    
    def turns(self):  # main game playing logic/
        if len(self.players) > 1 and self.round_count < 100:
            player = self.players[self.current_position]
            print(player.name + "'s turn")

            input("Press Enter to roll the dice: ")

            dice1, dice2 = self.roll_dice()
            print("First dice is " + str(dice1)) 
            print("Second dice is " + str(dice2))

            sum = dice1 + dice2
            print("Sum is " + str(sum))
            player.move(sum)  # player moves sum block
            
            

            
            # Check if the player landed on a property slot
            current_slot = player.board.selfposition(player.position)
            

            if isinstance(current_slot, Property_Slot) and current_slot.property.owner is not None: # if player lands on a owner's property
                current_slot.effect(player)
                
            elif isinstance(current_slot, Chance_Slot): # if player lands on a chance slot
                current_slot.effect(player)
                print(f"{player.name} landed on a Chance slot and now has {player.money} money.")
            elif isinstance(current_slot, Gotojail_Slot): # if player lands on a go to jail slot
                current_slot.effect(player)
                print(f"{player.name} is sent to jail.")
            elif isinstance(current_slot, Goslot):
                current_slot.effect(player)
                print(f"{player.name} stopped on Go. {player.name}'s money now is: {player.money}")
            elif isinstance(current_slot, Tax_Slot):
                current_slot.effect(player)
                print(f"{player.name} paid tax. {player.name}'s money now is: {player.money}")
            elif isinstance(current_slot, Free_Parking_Slot):
                current_slot.effect(player)
                print(f"{player.name} landed on Free Parking.")
            elif isinstance(current_slot, Visiting_Slot):
                current_slot.effect(player)
                print(f"{player.name} Just Visiting.")
            #if players money is less than 0, gets eliminated
            if player.money < 0:
                self.players.remove(player)
                print("Player Eliminated")
        
            self.current_position = (self.current_position + 1) % len(self.players)
            self.turn_count +=1 # have not tested yet

            # Display all players' money and position in CLI

            player_positions = [p.position for p in self.players]
            # Display all players' money and position in UI
            mainscreen(player_positions)


            for p in self.players:
                print(f"{p.name}'s money: {p.money}")  # print each player's money
                print(f"{p.name}'s position: {p.position + 1}")  # print each player's position
            print("\n")
        else:
            self.end_game()
    
    def end_game(self):
        if len(self.players) == 1:
            print(f"The game ended! {self.players[0].name} wins!")
        else:
            print("Game ended after 100 rounds.")
        user_input = input("Press Enter to exit: ")
        if user_input == "":
            sys.exit()
