import unittest
from yatzy import Yatzy

class TestYatzy(unittest.TestCase):
    def setUp(self):
        self.game = Yatzy()

    def test_ones(self):
        self.game.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.game.ones(), 1)

    def test_twos(self):
        self.game.dice = [2, 2, 3, 4, 5]
        self.assertEqual(self.game.twos(), 4)

    def test_threes(self):
        self.game.dice = [3, 3, 3, 4, 5]
        self.assertEqual(self.game.threes(), 9)

    def test_fours(self):
        self.game.dice = [4, 4, 4, 4, 5]
        self.assertEqual(self.game.fours(), 16)

    def test_fives(self):
        self.game.dice = [5, 5, 5, 5, 5]
        self.assertEqual(self.game.fives(), 25)

    def test_sixes(self):
        self.game.dice = [6, 6, 6, 6, 6]
        self.assertEqual(self.game.sixes(), 36)

    def test_one_pair(self):
        self.game.dice = [1, 2, 3, 4, 4]
        self.assertEqual(self.game.one_pair(), 8)

    def test_two_pairs(self):
        self.game.dice = [1, 1, 2, 3, 3]
        self.assertEqual(self.game.two_pairs(), 8)

    def test_three_alike(self):
        self.game.dice = [2, 2, 2, 3, 4]
        self.assertEqual(self.game.three_alike(), 6)

    def test_four_alike(self):
        self.game.dice = [2, 2, 2, 2, 4]
        self.assertEqual(self.game.four_alike(), 8)

    def test_small_straight(self):
        self.game.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.game.small_straight(), 15)

    def test_large_straight(self):
        self.game.dice = [2, 3, 4, 5, 6]
        self.assertEqual(self.game.large_straight(), 20)

    def test_full_house(self):
        self.game.dice = [1, 1, 2, 2, 2]
        self.assertEqual(self.game.full_house(), 8)

    def test_chance(self):
        self.game.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.game.chance(), 15)

    def test_yatzy(self):
        self.game.dice = [5, 5, 5, 5, 5]
        self.assertEqual(self.game.yatzy(), 50)

if __name__ == '__main__':
    unittest.main()