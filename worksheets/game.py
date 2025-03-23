from yatzy import Yatzy

def play_game():
    game = Yatzy()
    print("Initial roll:", game.dice)

    # Lock the first die and roll again
    game.lock_die(0)
    game.roll()
    print("After locking die 0 and rolling:", game.dice)

    # Unlock the first die and roll again
    game.unlock_die(0)
    game.roll()
    print("After unlocking die 0 and rolling:", game.dice)

    # Print scores for all methods
    print("Ones:", game.ones())
    print("Twos:", game.twos())
    print("Threes:", game.threes())
    print("Fours:", game.fours())
    print("Fives:", game.fives())
    print("Sixes:", game.sixes())
    print("One Pair:", game.one_pair())
    print("Two Pairs:", game.two_pairs())
    print("Three Alike:", game.three_alike())
    print("Four Alike:", game.four_alike())
    print("Small Straight:", game.small_straight())
    print("Large Straight:", game.large_straight())
    print("Full House:", game.full_house())
    print("Chance:", game.chance())
    print("Yatzy:", game.yatzy())

if __name__ == "__main__":
    play_game()