# from player import Playerclass
 #from monopoly import Monopolyclass
from All_slot import Goslot, Property_Slot, Chance_Slot, Tax_Slot, Visiting_Slot, Free_Parking_Slot, Gotojail_Slot
#Board 
class Boardclass:
    def __init__(self):
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
    