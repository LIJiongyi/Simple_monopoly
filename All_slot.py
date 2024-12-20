import random
import sys
# from monopoly import Monopolyclass
#from player import Playerclass
#from board import Boardclass

class Property:
    def __init__(self, name, rent, price):
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
    def __init__(self, position, name):
        self.position = position
        self.name = name

    def effect(self, player):
        player.money += 1500

#
class Property_Slot(Slot):
    def __init__(self, position, name, price, rent):
        self.position = position
        self.name = name
        self.price = price
        self.rent = rent
        self.property = Property(name, price, rent)

    def propertyactivity(self, rent, name, price):
        super().slotinfo(name, "property")
        self.property = self.property(name, price, rent)

    def effect(self, player):
        if self.property.owner is None:
            decision = input(f"Do you want to purchase {self.property.name} for {self.property.price}? (yes/no): ").strip().lower()
            if decision == 'yes':
                player.purchase(self.property)
                print(f"{player.name} purchased {self.property.name}. {player.name}'s money now is: {player.money}")
            else:
                print(f"{player.name} chose not to purchase {self.property.name}")
        elif self.property.owner != player:
            player.payrent(self.property)
            print(f"{player.name} paid rent to {self.property.owner.name}. {player.name}'s money now is: {player.money}")
#Randomly add or sub from the players money (either gain up to 200hkd or lose up to 300hkd)
class Chance_Slot(Slot):
    def __init__(self, position, name):
        self.position = position
        self.name = name

    def effect(self, player):
        addsub = random.choice(range(-300, 210, 10))
        player.money += addsub

# Pay 10% of player total money
class Tax_Slot(Slot):
    def __init__(self, position, name):
        self.position = position
        self.name = name

    def effect(self, player):
        tax = (player.money // 10) * 10
        player.money -= tax

class Free_Parking_Slot(Slot):
    def __init__(self, position, name):
        self.position = position
        self.name = name

    def effect(self, player):
        pass

class Visiting_Slot(Slot):
    def __init__(self, position, name):
        self.position = position
        self.name = name

    def effect(self, player):
        pass

class Gotojail_Slot(Slot):
    def __init__(self, position, name):
        self.position = position
        self.name = name

    def effect(self, player):
        player.injail()

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



        



