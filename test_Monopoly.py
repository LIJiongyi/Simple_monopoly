import unittest
from monopoly_game_logic import Monopolyclass
from Board_back import Boardclass, Property_Slot
from Player import Playerclass
from All_slot import Property, Chance_Slot, Tax_Slot, Goslot, Free_Parking_Slot, Visiting_Slot, Gotojail_Slot


class TestProperty(unittest.TestCase):
    def setUp(self):
        self.property = Property("Test Property", 500, 100)

    def test_property_initialization(self):
        """Test property initialization"""
        self.assertEqual(self.property.name, "Test Property")
        self.assertEqual(self.property.rent, 500)
        self.assertEqual(self.property.price, 100)
        self.assertIsNone(self.property.owner)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Boardclass()
        self.player = Playerclass("Test Player", self.board)
        self.property = Property("Test Property", 50, 100)

    def test_player_initialization(self):
        """Test player initialization"""
        self.assertEqual(self.player.money, 1500)
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.position, 0)
        self.assertEqual(len(self.player.properties), 0)
        self.assertFalse(self.player.jail)
        self.assertEqual(self.player.jailturns, 0)

    def test_player_movement(self):
        """Test player movement"""
        initial_position = self.player.position
        self.player.move(5)
        self.assertEqual(self.player.position, (initial_position + 5) % 20)

    def test_player_purchase(self):
        """Test property purchase"""
        initial_money = self.player.money
        self.player.purchase(self.property)
        self.assertEqual(self.player.money, initial_money - self.property.price)
        self.assertIn(self.property, self.player.properties)
        self.assertEqual(self.property.owner, self.player)

    def test_player_pay_rent(self):
        """Test rent payment"""
        owner = Playerclass("Owner", self.board)
        self.property.owner = owner
        initial_money = self.player.money
        owner_initial_money = owner.money

        self.player.payrent(self.property)

        self.assertEqual(self.player.money, initial_money - self.property.rent)
        self.assertEqual(owner.money, owner_initial_money + self.property.rent)

    def test_jail_mechanics(self):
        """Test jail-related mechanics"""
        self.player.injail()
        self.assertTrue(self.player.jail)
        self.assertEqual(self.player.position, 6)
        self.assertEqual(self.player.jailturns, 0)

        self.player.outjail()
        self.assertFalse(self.player.jail)
        self.assertEqual(self.player.jailturns, 0)


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Boardclass()

    def test_board_initialization(self):
        """Test board initialization"""
        self.assertEqual(len(self.board.locations), 20)
        self.assertIsInstance(self.board.locations[0], Goslot)
        self.assertIsInstance(self.board.locations[1], Property_Slot)

    def test_self_position(self):
        """Test position retrieval"""
        for i in range(20):
            slot = self.board.selfposition(i)
            self.assertEqual(slot, self.board.locations[i])


class TestMonopolyGame(unittest.TestCase):
    def setUp(self):
        self.game = Monopolyclass()

    def test_game_initialization(self):
        """Test game initialization"""
        self.assertEqual(len(self.game.players), 0)
        self.assertEqual(self.game.round_count, 0)
        self.assertEqual(self.game.turn_count, 0)
        self.assertEqual(self.game.current_position, 0)
        self.assertEqual(self.game.dice1, 0)
        self.assertEqual(self.game.dice2, 0)
        self.assertFalse(self.game.dice_rolled)

    def test_add_player(self):
        """Test adding players"""
        self.game.add_player("Player 1")
        self.assertEqual(len(self.game.players), 1)
        self.assertEqual(self.game.players[0].name, "Player 1")

    def test_roll_dice(self):
        """Test dice rolling"""
        dice1, dice2 = self.game.roll_dice()
        self.assertTrue(1 <= dice1 <= 6)
        self.assertTrue(1 <= dice2 <= 6)


class TestSlots(unittest.TestCase):
    def setUp(self):
        self.board = Boardclass()
        self.player = Playerclass("Test Player", self.board)

    def test_go_slot(self):
        """Test Go slot effect"""
        go_slot = Goslot(0, "Go")
        initial_money = self.player.money
        go_slot.effect(self.player)
        self.assertEqual(self.player.money, initial_money + 1500)

    def test_tax_slot(self):
        """Test Tax slot effect"""
        tax_slot = Tax_Slot(4, "Tax")
        initial_money = self.player.money
        tax_slot.effect(self.player)
        expected_money = initial_money - ((initial_money // 10) * 10)
        self.assertEqual(self.player.money, expected_money)

    def test_chance_slot(self):
        """Test Chance slot effect"""
        chance_slot = Chance_Slot(9, "Chance")
        initial_money = self.player.money
        chance_slot.effect(self.player)
        self.assertTrue(-300 <= self.player.money - initial_money <= 200)

    def test_jail_slot(self):
        """Test Go to Jail slot effect"""
        jail_slot = Gotojail_Slot(16, "Go to Jail")
        jail_slot.effect(self.player)
        self.assertTrue(self.player.jail)
        self.assertEqual(self.player.position, 6)


def run_tests():
    """Run all tests"""
    test_classes = [
        TestProperty,
        TestPlayer,
        TestBoard,
        TestMonopolyGame,
        TestSlots
    ]

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    run_tests()