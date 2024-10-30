import random
import sys

# Players stats
class Player:
    def __init__(self, name): # previous "participant" switch to init
        self.money = 1500
        self.name = name
        self.position = 0
        self.properties = []
        self.jail = False
        self.jailturns = 0

    def move(self, step):
        self.position = (self.position + step) % 20
        current_slot = board.selfposition(self.position) 
        current_slot.effect(self)

    def purchase(self, property):
        if self.money >= property.price and property.owner is None:
            self.money = self.money - property.price
            self.properties.append(property)
            property.owner = self

    def payrent(self, property):
        if property.owner != self:
            rent = property.rent
            self.money -= rent
            property.owner.money += rent

    def injail(self):
        self.jail = True
        self.position = 6
        self.jailturns = 0

    def outjail(self):
        self.jail = False
        self.jailturns = 0
    
class Property:
    def propinfo(self, name, rent, price):
        self.name = name
        self.rent = rent
        self.price = price
        self.owner = None

class Slot:
    def slotinfo(self, name, kind):
        self.name = name
        self.kind = kind

    def effect(self, player):
        pass

#add 1500 to player toyal money
class Goslot(Slot):
    def effect(player, self):
        player.money += 1500

#
class Property_Slot(Slot):
    def propertyactivity(self, rent, name, price):
        super().slotinfo(name, "property")
        self.property = self.property(name, price, rent)

    def effect(self, player):
        if self.property.owner is None:
            player.purchase(self.property)
        elif self.property.owner != None:
            player.payrent(self.property)

#Randomly add or sub from the players money (either gain up to 200hkd or lose up to 300hkd)
class Chance_Slot(Slot):
    def effect(self, player):
        addsub = random.choice(range(-300, 210, 10))
        player.money += addsub

#Pay 10% of player total money
class Tax_Slot(Slot):
    def effect(self, player):
        tax = (player.money // 10) * 10
        player.money -= tax

class Free_Parking_Slot(Slot):
    def effect(self, player):
        pass

class Visiting_Slot:
    def effect(self, player):
        pass

class Gotojail_Slot(Slot):
    def effect(self, player):
        player.gojail()

class Jail_Slot(Slot):
    def double(self):
        return random.randint(1,6) == random.randint(1,6)

    def throwdice(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dicesum = dice1 + dice2
        return dicesum

    def effect(self, player):
        if player.injail:
            player.jailturns += 1
            if player.jailturns <= 3 and player.money >= 150:
                decision = input("Pay 150 to get out of jail? (yes/no)").strip().lower()
                if decision == 'yes':
                    player.money -= 150
                    player.outjail()
                    rolldice = self.throwdice
                    player.move(rolldice)
            if player.jailturns == 3:
                player.money -= 150
                player.outjail()
                rolldice = self.throwdice
                player.move(rolldice)
            elif self.double:
                player.outjail()
                rolldice = self.throwdice
                player.move(rolldice)

#Board 
class board:
    def slots(self):
        self.locations = [
            Goslot(1,"Go"),
            Property_Slot(2, "Central", 800, 90),
            Property_Slot(3, "Wan Chai", 700, 65),
            Tax_Slot(4, "INCOME TAX"),
            Property_Slot(5,"Stanley", 600, 60),
            Visiting_Slot(6, "JUST VISITING"),
            Property_Slot(7, "Chek O", 400, 10),
            Property_Slot(8, "Mong Kok", 500, 40),
            Chance_Slot(9, "Chance"),
            Property_Slot(10, "Tsing Yi", 400, 15),
            Free_Parking_Slot(11, "Free Parking"),
            Property_Slot(12, "Shatin", 700, 75),
            Chance_Slot(13, "Chance"),
            Property_Slot(14, "Tuen Mun", 400, 20),
            Property_Slot(15, "Tai Po", 500, 25),
            Gotojail_Slot(16, "Go to jail"),
            Property_Slot(17, "Sai Kung", 400, 10),
            Property_Slot(18, "Yuen Long", 400, 25),
            Chance_Slot(19, "Chance"),
            Property_Slot(20, "Tai O", 600, 25),
        ]

    def selfposition(self, position):
        return self.locations[position]
    
# Game Logic
class Monopoly:
    def start(self):
        self.board = board()
        self.players = []
        self.current_position = 0
        self.round_count = 0  # count round
        self.turn_count = 0

    # Add players
    def add_player(self, name):
        self. players.append(Player(name))

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
        


#Player management
def Start_game(board_instance: board, monopoly_game: Monopoly):
    # global board_instance 
    # board_instance = board()
    # monopoly_game = Monopoly()

    # adds player up to 8, type 'done' to finish adding more players
    print("Enter player names (max 8 players). Type 'done' when finished:")
    while len(monopoly_game.players) < 8:
        name = input(f"Player {len(monopoly_game.players) + 1}: ")
        if name:  # Ensure the name is not empty
            monopoly_game.add_player(name)
        if name.lower() == 'done':
            break
        
        # loop until only 1 player is left
        while True: 
            monopoly_game.turns()

        # if len(monopoly_game.players) == 1:
        #     print(f"The game ended! {monopoly_game.players[0].name} wins!")
