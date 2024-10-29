import random
import sys

# Players stats
class Player:
    def __init__(my, name): # previous "participant" switch to init
        my.money = 1500
        my.name = name
        my.position = 0
        my.properties = []
        my.jail = False
        my.jailturns = 0

    def move(my, step):
        my.position = (my.position + step) % 20
        current_slot = board.myposition(my.position) 
        current_slot.effect(my)

    def purchase(my, property):
        if my.money >= property.price and property.owner is None:
            my.money = my.money - property.price
            my.properties.append(property)
            property.owner = my

    def payrent(my, property):
        if property.owner != my:
            rent = property.rent
            my.money -= rent
            property.owner.money += rent

    def injail(my):
        my.jail = True
        my.position = 6
        my.jailturns = 0

    def outjail(my):
        my.jail = False
        my.jailturns = 0
    
class Property:
    def propinfo(my, name, rent, price):
        my.name = name
        my.rent = rent
        my.price = price
        my.owner = None

class Slot:
    def slotinfo(my, name, kind):
        my.name = name
        my.kind = kind

    def effect(my, player):
        pass

#add 1500 to player toyal money
class Goslot(Slot):
    def effect(player, my):
        player.money += 1500

#
class Property_Slot(Slot):
    def propertyactivity(my, rent, name, price):
        super().slotinfo(name, "property")
        my.property = my.property(name, price, rent)

    def effect(my, player):
        if my.property.owner is None:
            player.purchase(my.property)
        elif my.property.owner != None:
            player.payrent(my.property)

#Randomly add or sub from the players money (either gain up to 200hkd or lose up to 300hkd)
class Chance_Slot(Slot):
    def effect(my, player):
        addsub = random.choice(range(-300, 210, 10))
        player.money += addsub

#Pay 10% of player total money
class Tax_Slot(Slot):
    def effect(my, player):
        tax = (player.money // 10) * 10
        player.money -= tax

class Free_Parking_Slot(Slot):
    def effect(my, player):
        pass

class Visiting_Slot:
    def effect(my, player):
        pass

class Gotojail_Slot(Slot):
    def effect(my, player):
        player.gojail()

class Jail_Slot(Slot):
    def double(my):
        return random.randint(1,6) == random.randint(1,6)

    def throwdice(my):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dicesum = dice1 + dice2
        return dicesum

    def effect(my, player):
        if player.injail:
            player.jailturns += 1
            if player.jailturns <= 3 and player.money >= 150:
                decision = input("Pay 150 to get out of jail? (yes/no)").strip().lower()
                if decision == 'yes':
                    player.money -= 150
                    player.outjail()
                    rolldice = my.throwdice
                    player.move(rolldice)
            if player.jailturns == 3:
                player.money -= 150
                player.outjail()
                rolldice = my.throwdice
                player.move(rolldice)
            elif my.double:
                player.outjail()
                rolldice = my.throwdice
                player.move(rolldice)

#Board 
class board:
    def slots(my):
        my.locations = [
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

    def myposition(my, position):
        return my.locations[position]
    
# Game Logic
class Monopoly:
    def start(my):
        my.board = board()
        my.players = []
        my.current_position = 0
        my.round_count = 0  # count round

    # Add players
    def add_player(my, name):
        my. players.append(Player(name))

    # Roll dices
    def roll_dice(my):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        return dice1, dice2

    # player roll 2 dices and move accordin to the sum of both dices    
    def turns(my):
        if len(my.players)>1 and my.round_count <100:
            player = my.players[my.current_position]
            print(player.name + "'s turn")
        
            dice1, dice2 = my.roll_dice()
            print("First dice is " + dice1)
            print("First dice is " + dice2)

            sum = dice1 + dice2
            print("Sum is " + sum)
            player.move(sum)  # player moves sum block

            #if players money is less than 0, gets eliminated
            if player.money < 0:
                my.players.remove(player)
                print("Player Eliminated")
        
            my.current_position = (my.current_position + 1) % len(my.players)
            my.round_count +=1 # not sure if it is right to add riaht here, check again first
        else:
            my.end_game
    
    def end_game(my):
        if len(my.players) == 1:
            print(f"The game ended! {my.players[0].name} wins!")
        else:
            print("Game ended after 100 rounds.")
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
        while len(monopoly_game.players) > 1 and monopoly_game.round_count < 100: 
            monopoly_game.play_turn()

        if len(monopoly_game.players) == 1:
            print(f"The game ended! {monopoly_game.players[0].name} wins!")
