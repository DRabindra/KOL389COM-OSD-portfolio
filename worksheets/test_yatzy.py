import unittest
from yatzy import Yatzy
import time

class TestYatzy(unittest.TestCase):
    """This class tests all the Yatzy game functionality"""
    
    def setUp(self):
        """Setup a new game before each test"""
        print("\nSetting up new game...", end=" ")
        self.game = Yatzy()
        print("Done!")
        time.sleep(0.1)  # Makes it feel more "real"
    
    # Test 1: Basic dice rolling
    def test_dice_rolling(self):
        """Check if dice rolling works properly"""
        print("\nTest 1: Checking dice rolling...")
        first_roll = self.game.dice.copy()
        
        # Second roll should change some dice
        self.game.roll()
        second_roll = self.game.dice
        
        # At least one die should change (unless all were locked)
        self.assertNotEqual(first_roll, second_roll, 
                          "Dice didn't change after roll!")
        print("✓ Roll test passed")
    
    # Test 2: Locking mechanism
    def test_dice_locking(self):
        """Test if locking dice works"""
        print("\nTest 2: Testing dice locking...")
        self.game.dice = [1,2,3,4,5]  # Set fixed values for testing
        
        # Lock first die
        self.game.lock_die(0)
        self.game.roll()
        
        # Die 0 should stay the same, others change
        self.assertEqual(self.game.dice[0], 1,
                        "Locked die changed!")
        print("✓ Lock test passed")
    
    # Test 3: Scoring - Ones to Sixes
    def test_basic_scoring(self):
        """Test all number categories (ones to sixes)"""
        print("\nTest 3: Testing basic scoring...")
        test_cases = [
            ([1,1,2,2,2], "ones", 2),
            ([2,2,2,4,5], "twos", 6),
            ([6,6,6,6,6], "sixes", 30)  # Fixed from earlier bug!
        ]
        
        for dice, category, expected in test_cases:
            with self.subTest(category=category):
                self.game.dice = dice
                result = getattr(self.game, category)()
                self.assertEqual(result, expected,
                               f"{category} scoring failed!")
        print("✓ Basic scoring passed")
    
    # Test 4: Special categories
    def test_special_categories(self):
        """Test pairs, straights, full house etc."""
        print("\nTest 4: Testing special categories...")
        cases = [
            ([1,1,2,3,4], "one_pair", 2),
            ([2,2,3,3,4], "two_pairs", 10),
            ([1,1,1,4,5], "three_alike", 3),
            ([1,1,1,1,5], "four_alike", 4),
            ([1,2,3,4,5], "small_straight", 15),
            ([2,3,4,5,6], "large_straight", 20),
            ([1,1,2,2,2], "full_house", 8),
            ([1,2,3,4,5], "chance", 15),
            ([5,5,5,5,5], "yatzy", 50)
        ]
        
        for dice, category, expected in cases:
            with self.subTest(category=category):
                self.game.dice = dice
                result = getattr(self.game, category)()
                self.assertEqual(result, expected,
                               f"{category} failed!")
        print("✓ Special categories passed")
    
    # Test 5: Edge cases
    def test_edge_cases(self):
        """Test with no possible scores"""
        print("\nTest 5: Testing edge cases...")
        no_score_dice = [1,2,3,4,6]  # No pairs or specials
        self.game.dice = no_score_dice
        
        self.assertEqual(self.game.one_pair(), 0,
                        "Found pair where none exists!")
        self.assertEqual(self.game.full_house(), 0,
                        "Found full house where none exists!")
        print("✓ Edge cases passed")

# Simple way to run tests with different verbosity
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true",
                       help="Show detailed test output")
    args = parser.parse_args()
    
    if args.verbose:
        unittest.main(verbosity=2)
    else:
        # Simple student-friendly output
        print("\n" + "="*50)
        print("Running Yatzy Tests...")
        print("="*50)
        test_runner = unittest.TextTestRunner(verbosity=0)
        suite = unittest.TestLoader().loadTestsFromTestCase(TestYatzy)
        result = test_runner.run(suite)
        
        # Simple summary
        print("\nTest Summary:")
        print(f"Passed: {result.testsRun - len(result.failures)}")
        print(f"Failed: {len(result.failures)}")
        if result.wasSuccessful():
            print("\n✅ All tests passed! Good job!")
        else:
            print("\n❌ Some tests failed. Check your code!")