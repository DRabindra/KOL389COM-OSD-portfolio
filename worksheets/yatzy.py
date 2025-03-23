import random

class Yatzy:
    def __init__(self):
        self.dice = [0] * 5  # Initialize 5 dice
        self.locked = [False] * 5  # Track locked dice
        self.roll()  # Roll all dice on initialization

    def roll(self):
        """Roll all unlocked dice."""
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)

    def lock_die(self, index):
        """Lock a specific die."""
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock_die(self, index):
        """Unlock a specific die."""
        if 0 <= index < 5:
            self.locked[index] = False

    # Scoring methods
    def ones(self):
        return self.dice.count(1) * 1

    def twos(self):
        return self.dice.count(2) * 2

    def threes(self):
        return self.dice.count(3) * 3

    def fours(self):
        return self.dice.count(4) * 4

    def fives(self):
        return self.dice.count(5) * 5

    def sixes(self):
        return self.dice.count(6) * 6

    def one_pair(self):
        for value in range(6, 0, -1):
            if self.dice.count(value) >= 2:
                return value * 2
        return 0

    def two_pairs(self):
        pairs = []
        for value in range(6, 0, -1):
            if self.dice.count(value) >= 2:
                pairs.append(value)
                if len(pairs) == 2:
                    return sum(pairs) * 2
        return 0

    def three_alike(self):
        for value in range(6, 0, -1):
            if self.dice.count(value) >= 3:
                return value * 3
        return 0

    def four_alike(self):
        for value in range(6, 0, -1):
            if self.dice.count(value) >= 4:
                return value * 4
        return 0

    def small_straight(self):
        if sorted(self.dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    def large_straight(self):
        if sorted(self.dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    def full_house(self):
        counts = {x: self.dice.count(x) for x in set(self.dice)}
        if sorted(counts.values()) == [2, 3]:
            return sum(self.dice)
        return 0

    def chance(self):
        return sum(self.dice)

    def yatzy(self):
        if all(d == self.dice[0] for d in self.dice):
            return 50
        return 0