import random
from Player import Playerclass
from Board_back import Boardclass, Property_Slot  # note that the first word can also be uppercase, it is a OS system(Windows,Unix)
import sys

# Game Logic
class Monopolyclass:
    def __init__(self):
        self.players = []
        self.round_count = 0  # count round
        self.turn_count = 0
        self.current_position = 0
        self.board = Boardclass()

    # def start(self):
        
        
    # Add players
    def add_player(self, name):
        self.players.append(Playerclass(name, self.board))

    # Roll dices
    def roll_dice(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        return dice1, dice2

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
            
            # print(f"{player.name}'s money: {player.money}")  # testing, print player's money  (we can remove this now)
            # print(f"{player.name}'s position: {player.position + 1}")  # testing, print player's position

            # Display all players' money and position
            for p in self.players:
                print(f"{p.name}'s money: {p.money}")  # print each player's money
                print(f"{p.name}'s position: {p.position + 1}")  # print each player's position

            # Check if the player landed on a property slot
            current_slot = player.board.selfposition(player.position)
            if isinstance(current_slot, Property_Slot) and current_slot.property.owner is None:
                decision = input(f"Do you want to purchase {current_slot.property.name} for {current_slot.property.price}? (yes/no): ").strip().lower()
                if decision == 'yes':
                    player.purchase(current_slot.property)
                    print(f"{player.name}'s money now is: {player.money}")
                else:
                    print(f"{player.name} chose not to purchase {current_slot.property.name}")

            #if players money is less than 0, gets eliminated
            if player.money < 0:
                self.players.remove(player)
                print("Player Eliminated")
        
            self.current_position = (self.current_position + 1) % len(self.players)
            self.turn_count +=1 # not sure if it is right to add riaht here, check again first
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