import random
import time

class NumberGuessingGame:
    def __init__(self):
        self.games_played = 0
        self.total_score = 0
        self.best_score = float('inf')
        self.difficulty_levels = {
            '1': {'name': 'Easy', 'range': (1, 50), 'max_attempts': 10},
            '2': {'name': 'Medium', 'range': (1, 100), 'max_attempts': 8},
            '3': {'name': 'Hard', 'range': (1, 200), 'max_attempts': 6},
            '4': {'name': 'Expert', 'range': (1, 500), 'max_attempts': 5}
        }
    
    def display_welcome(self):
        print("=" * 50)
        print("🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯")
        print("=" * 50)
        print("I'm thinking of a number... Can you guess it?")
        print("The fewer attempts you use, the higher your score!")
        print()
    
    def display_stats(self):
        if self.games_played > 0:
            avg_score = self.total_score / self.games_played
            print(f"\n📊 YOUR STATISTICS:")
            print(f"Games Played: {self.games_played}")
            print(f"Average Score: {avg_score:.1f}")
            print(f"Best Score: {self.best_score}")
        print()
    
    def choose_difficulty(self):
        print("Choose your difficulty level:")
        for key, value in self.difficulty_levels.items():
            range_min, range_max = value['range']
            print(f"{key}. {value['name']} - Numbers {range_min}-{range_max} ({value['max_attempts']} attempts)")
        
        while True:
            choice = input("\nEnter difficulty (1-4): ").strip()
            if choice in self.difficulty_levels:
                return self.difficulty_levels[choice]
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
    
    def get_hint(self, guess, target):
        diff = abs(guess - target)
        if diff == 0:
            return "🎉 PERFECT!"
        elif diff <= 5:
            return "🔥 Very Hot!"
        elif diff <= 10:
            return "🌡️ Hot!"
        elif diff <= 20:
            return "🟡 Warm"
        elif diff <= 50:
            return "🧊 Cold"
        else:
            return "❄️ Very Cold!"
    
    def calculate_score(self, attempts, max_attempts, difficulty_multiplier):
        # Base score decreases with more attempts
        base_score = max(100 - (attempts - 1) * 10, 10)
        # Bonus for finishing with attempts remaining
        bonus = (max_attempts - attempts) * 5
        # Difficulty multiplier
        total_score = (base_score + bonus) * difficulty_multiplier
        return int(total_score)
    
    def play_round(self):
        difficulty = self.choose_difficulty()
        range_min, range_max = difficulty['range']
        max_attempts = difficulty['max_attempts']
        difficulty_multiplier = {'Easy': 1, 'Medium': 1.2, 'Hard': 1.5, 'Expert': 2}[difficulty['name']]
        
        target_number = random.randint(range_min, range_max)
        attempts = 0
        
        print(f"\n🎮 Starting {difficulty['name']} mode!")
        print(f"I'm thinking of a number between {range_min} and {range_max}")
        print(f"You have {max_attempts} attempts. Good luck!")
        print("-" * 40)
        
        start_time = time.time()
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
                attempts += 1
                
                if guess < range_min or guess > range_max:
                    print(f"⚠️ Please guess between {range_min} and {range_max}!")
                    attempts -= 1  # Don't count invalid guesses
                    continue
                
                if guess == target_number:
                    end_time = time.time()
                    time_taken = round(end_time - start_time, 1)
                    
                    print(f"\n🎉 CONGRATULATIONS! 🎉")
                    print(f"You guessed {target_number} in {attempts} attempts!")
                    print(f"Time taken: {time_taken} seconds")
                    
                    score = self.calculate_score(attempts, max_attempts, difficulty_multiplier)
                    print(f"Your score: {score} points")
                    
                    # Update statistics
                    self.games_played += 1
                    self.total_score += score
                    if score < self.best_score:
                        self.best_score = score
                        print("🏆 NEW BEST SCORE! 🏆")
                    
                    return True
                
                elif guess < target_number:
                    print(f"📈 Too low! {self.get_hint(guess, target_number)}")
                else:
                    print(f"📉 Too high! {self.get_hint(guess, target_number)}")
                
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"Attempts remaining: {remaining}")
                
            except ValueError:
                print("❌ Please enter a valid number!")
                attempts -= 1  # Don't count invalid input
        
        # Game over - ran out of attempts
        print(f"\n💀 Game Over! You've used all {max_attempts} attempts.")
        print(f"The number was: {target_number}")
        self.games_played += 1
        return False
    
    def play_game(self):
        self.display_welcome()
        
        while True:
            self.display_stats()
            
            play = input("Would you like to play a round? (y/n): ").lower().strip()
            if play not in ['y', 'yes']:
                break
            
            won = self.play_round()
            
            if won:
                print("\n🌟 Great job! Want to try a harder difficulty?")
            else:
                print("\n🎯 Don't give up! Practice makes perfect!")
        
        print(f"\n🎮 Thanks for playing!")
        if self.games_played > 0:
            print("Final Statistics:")
            self.display_stats()
        print("See you next time! 👋")

def main():
    game = NumberGuessingGame()
    game.play_game()

if __name__ == "__main__":
    main()