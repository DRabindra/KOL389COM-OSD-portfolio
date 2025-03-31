import random

class Yatzy:
    def __init__(self):
        self.dice = [0] * 5
        self.locked = [False] * 5
        self.roll_count = 0
        self.roll()  # Initial roll

    def roll(self):
        """Roll all unlocked dice and increment roll count"""
        if self.roll_count >= 3:
            raise ValueError("Maximum 3 rolls per turn")
            
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)
        self.roll_count += 1
        return self.dice.copy()

    def lock_die(self, index):
        """Lock a specific die (0-4)"""
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock_die(self, index):
        """Unlock a specific die (0-4)"""
        if 0 <= index < 5:
            self.locked[index] = False

    def reset_turn(self):
        """Reset locks and roll count for new turn"""
        self.locked = [False] * 5
        self.roll_count = 0

    # Scoring methods
    def ones(self): return self._sum_numbers(1)
    def twos(self): return self._sum_numbers(2)
    def threes(self): return self._sum_numbers(3)
    def fours(self): return self._sum_numbers(4)
    def fives(self): return self._sum_numbers(5)
    def sixes(self): return self._sum_numbers(6)
    
    def _sum_numbers(self, number):
        return self.dice.count(number) * number

    def one_pair(self):
        pairs = self._find_pairs()
        return max(pairs) * 2 if pairs else 0

    def two_pairs(self):
        pairs = sorted(self._find_pairs(), reverse=True)
        return sum(pairs[:2]) * 2 if len(pairs) >= 2 else 0

    def _find_pairs(self):
        return [num for num in range(1, 7) if self.dice.count(num) >= 2]

    def three_alike(self): return self._of_a_kind(3)
    def four_alike(self): return self._of_a_kind(4)
    
    def _of_a_kind(self, n):
        for num in range(6, 0, -1):
            if self.dice.count(num) >= n:
                return num * n
        return 0

    def small_straight(self):
        return 15 if sorted(self.dice) == [1,2,3,4,5] else 0

    def large_straight(self):
        return 20 if sorted(self.dice) == [2,3,4,5,6] else 0

    def full_house(self):
        counts = {x: self.dice.count(x) for x in set(self.dice)}
        if sorted(counts.values()) == [2,3]:
            return sum(self.dice)
        return 0

    def chance(self): return sum(self.dice)

    def yatzy(self):
        return 50 if all(d == self.dice[0] for d in self.dice) else 0