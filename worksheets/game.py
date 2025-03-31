from yatzy import Yatzy
import time
import sys

class YatzyGame:
    def __init__(self):
        self.game = Yatzy()
        self.scorecard = {}
        
    def show_dice(self):
        print("\nCurrent Dice:")
        for i, die in enumerate(self.game.dice):
            lock_status = " (Locked)" if self.game.locked[i] else ""
            print(f"  Die {i+1}: {die}{lock_status}")
            
    def show_scorecard(self):
        print("\nScorecard:")
        for category, score in self.scorecard.items():
            print(f"  {category}: {score}")
            
    def roll_animation(self):
        print("\nRolling", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print()
        
    def take_turn(self):
        self.game.reset_turn()
        print("\n=== New Turn ===")
        
        while self.game.roll_count < 3:
            cmd = input("\nCommand (roll/lock/unlock/score/quit): ").lower()
            
            if cmd == "roll":
                self.roll_animation()
                self.game.roll()
                self.show_dice()
                
            elif cmd.startswith("lock"):
                try:
                    die = int(cmd.split()[1]) - 1
                    self.game.lock_die(die)
                    self.show_dice()
                except:
                    print("Usage: lock 1-5")
                    
            elif cmd.startswith("unlock"):
                try:
                    die = int(cmd.split()[1]) - 1
                    self.game.unlock_die(die)
                    self.show_dice()
                except:
                    print("Usage: unlock 1-5")
                    
            elif cmd == "score":
                self.score_turn()
                return
                
            elif cmd == "quit":
                sys.exit()
                
        self.score_turn()
        
    def score_turn(self):
        self.show_dice()
        print("\nAvailable Categories:")
        categories = [m for m in dir(self.game) 
                     if not m.startswith('_') and callable(getattr(self.game, m))
                     and m not in ['roll', 'lock_die', 'unlock_die', 'reset_turn']]
        
        for i, cat in enumerate(categories):
            if cat not in self.scorecard:
                print(f"  {i+1}. {cat}")
                
        while True:
            try:
                choice = input("Choose category number: ")
                if choice == "quit":
                    sys.exit()
                    
                cat = categories[int(choice)-1]
                if cat in self.scorecard:
                    print("Category already used!")
                    continue
                    
                score = getattr(self.game, cat)()
                self.scorecard[cat] = score
                print(f"Scored {score} points for {cat}!")
                break
                
            except (ValueError, IndexError):
                print("Invalid choice. Try again or type 'quit'")

def main():
    print("""
    Welcome to Yatzy!
    Commands:
    - roll: Roll unlocked dice
    - lock 1-5: Lock a die
    - unlock 1-5: Unlock a die
    - score: End turn and choose category
    - quit: Exit game
    """)
    
    game = YatzyGame()
    while len(game.scorecard) < 13:  # All categories
        game.take_turn()
        game.show_scorecard()
        
    print("\nGame Over! Final Score:", sum(game.scorecard.values()))

if __name__ == "__main__":
    main()