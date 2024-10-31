import random
from player import Playerclass
from board import Boardclass
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
        self.players.append(Playerclass(name))

    # Roll dices
    def roll_dice(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        return dice1, dice2

    # player roll 2 dices and move accordin to the sum of both dices    
    def turns(self):  # main game playing logic/
        if len(self.players)>1 and self.round_count <100:
            player = self.players[self.current_position]
            print(player.name + "'s turn")
        
            dice1, dice2 = self.roll_dice()
            print("First dice is " + dice1)
            print("First dice is " + dice2)

            sum = dice1 + dice2
            print("Sum is " + sum)
            player.move(sum)  # player moves sum block

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