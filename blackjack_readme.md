# Simple Blackjack Game

A command-line implementation of the classic Blackjack card game written in Python. Test your luck and strategy against the dealer in this faithful recreation of the casino favorite!

## Features

- **Complete Deck Management**: Full 52-card deck with proper shuffling
- **Realistic Gameplay**: Follow standard Blackjack rules and dealer behavior
- **Chip System**: Start with 100 chips and bet on each hand
- **Smart Ace Handling**: Aces automatically adjust between 1 and 11 values
- **Interactive Controls**: Simple hit/stand decisions
- **Multiple Win Conditions**: Player wins, dealer wins, busts, and pushes
- **Continuous Play**: Keep playing until you run out of chips or choose to quit

## How to Play

### Basic Rules
- Get as close to 21 as possible without going over
- Face cards (Jack, Queen, King) are worth 10 points
- Aces are worth 11 or 1 (whichever is better for your hand)
- Dealer must hit until reaching 17 or higher
- Beat the dealer's hand without busting to win

### Game Flow
1. **Place Your Bet**: Choose how many chips to wager (you start with 100)
2. **Receive Cards**: You and the dealer each get 2 cards (one dealer card is hidden)
3. **Make Decisions**: Choose to Hit (take another card) or Stand (keep current hand)
4. **Dealer Plays**: If you don't bust, dealer plays automatically following house rules
5. **Determine Winner**: Compare hands and collect/lose chips accordingly

## Installation & Setup

### Requirements
- Python 3.6 or higher
- No external dependencies required (uses only built-in libraries)

### Running the Game
1. Save the code as `blackjack.py`
2. Open your terminal/command prompt
3. Navigate to the file location
4. Run the game:
   ```bash
   python blackjack.py
   ```

## Game Controls

During gameplay, you'll be prompted with simple commands:

- **Betting**: Enter a number for your chip bet
- **Hit or Stand**: Type `h` to hit or `s` to stand
- **Continue Playing**: Type `y` to play another hand or `n` to quit

## Code Structure

The game is organized into several classes and functions:

### Classes
- **Card**: Represents individual playing cards with suit, rank, and value
- **Deck**: Manages the full deck of cards, shuffling, and dealing
- **Hand**: Tracks cards in a player's hand and calculates total value

### Key Functions
- **Game Logic**: `hit()`, `hit_or_stand()`, `take_bet()`
- **Win Conditions**: `player_wins()`, `dealer_wins()`, `player_busts()`, `dealer_busts()`, `push()`
- **Display**: `show_chips()`, `show_all()`, `show_some()`

## Example Gameplay

```
Welcome to BlackJack! Get as close to 21 as you can without going over!
Dealer hits until she reaches 17. Aces count as 1 or 11.

Player's chips: 100

How many chips would you like to bet? (You have 100): 10

--- Dealer's Hand ---
Hidden Card
7 of Hearts

--- Cards in Hand ---
King of Spades
5 of Diamonds
Total Value: 15

Would you like to Hit or Stand? Enter 'h' or 's': h

--- Cards in Hand ---
King of Spades
5 of Diamonds
4 of Clubs
Total Value: 19

Would you like to Hit or Stand? Enter 'h' or 's': s
Player stands. Dealer is playing.

--- Final Results ---
--- Dealer's Hand ---
Queen of Hearts
7 of Hearts
Total Value: 17

--- Cards in Hand ---
King of Spades
5 of Diamonds
4 of Clubs
Total Value: 19

Player wins!

Player's chips: 110
```

## Strategy Tips

- **Basic Strategy**: Hit if your total is 11 or less, stand if 17 or more
- **Ace Management**: The game automatically optimizes ace values for you
- **Risk vs Reward**: Consider the dealer's visible card when making decisions
- **Bankroll Management**: Don't bet all your chips at once!

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Split functionality for pairs
- Double down option
- Multiple deck support
- GUI implementation
- Advanced betting strategies

---

Enjoy the game and may the cards be in your favor! 🃏