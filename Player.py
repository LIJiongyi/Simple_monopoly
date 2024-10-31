# Player class, Players stats
from board import Boardclass


class Playerclass:
    def __init__(self, name): # previous "participant" switch to init
        self.money = 1500
        self.name = name
        self.position = 0
        self.properties = []
        self.jail = False
        self.jailturns = 0

    def move(self, step):
        self.position = (self.position + step) % 20
        current_slot = Boardclass.selfposition(self.position) 
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