# 🎯 Number Guessing Game

A feature-rich, interactive number guessing game built in Python that challenges players to guess a randomly generated number with smart hints, multiple difficulty levels, and comprehensive scoring system.

## ✨ Features

- **🎮 4 Difficulty Levels**: From beginner-friendly to expert challenge
- **🏆 Smart Scoring System**: Rewards efficiency and difficulty selection
- **🌡️ Temperature Hints**: Get "hot/cold" feedback based on proximity to target
- **📊 Statistics Tracking**: Monitor your progress across multiple games
- **⏱️ Time Tracking**: See how quickly you can solve each puzzle
- **🎨 Colorful Interface**: Emoji-rich, engaging user experience
- **🛡️ Input Validation**: Robust error handling for smooth gameplay

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Installation & Running
1. Clone this repository or download the `number_guessing_game.py` file
2. Open your terminal/command prompt
3. Navigate to the file location
4. Run the game:
   ```bash
   python number_guessing_game.py
   ```

## 🎯 How to Play

### Game Objective
Guess the secret number in as few attempts as possible to maximize your score!

### Difficulty Levels

| Level | Range | Max Attempts | Score Multiplier |
|-------|-------|--------------|------------------|
| 🟢 Easy | 1-50 | 10 | 1.0x |
| 🟡 Medium | 1-100 | 8 | 1.2x |
| 🔴 Hard | 1-200 | 6 | 1.5x |
| 🟣 Expert | 1-500 | 5 | 2.0x |

### Gameplay Flow
1. **Select Difficulty**: Choose your challenge level
2. **Make Guesses**: Enter numbers within the specified range
3. **Receive Feedback**: Get directional hints and temperature clues
4. **Win or Lose**: Guess correctly before running out of attempts
5. **View Stats**: Track your performance across games

## 🌡️ Hint System

The game provides proximity-based hints to guide your guesses:

- 🎉 **Perfect!** - You got it exactly right!
- 🔥 **Very Hot!** - Within 5 numbers of the target
- 🌡️ **Hot!** - Within 10 numbers of the target
- 🟡 **Warm** - Within 20 numbers of the target
- 🧊 **Cold** - Within 50 numbers of the target
- ❄️ **Very Cold!** - More than 50 numbers away

## 🏆 Scoring System

Your score is calculated based on:

**Base Score**: Starts at 100, decreases by 10 for each attempt
**Bonus Points**: 5 points for each unused attempt
**Difficulty Multiplier**: Applied based on chosen difficulty level

**Formula**: `(Base Score + Bonus) × Difficulty Multiplier`

### Example Scoring
- Easy mode, 3 attempts used, 7 remaining: `(80 + 35) × 1.0 = 115 points`
- Expert mode, 2 attempts used, 3 remaining: `(90 + 15) × 2.0 = 210 points`

## 📊 Statistics

The game tracks your performance with:
- **Games Played**: Total number of completed games
- **Average Score**: Mean score across all games
- **Best Score**: Your highest score achieved
- **Time Tracking**: Duration for each successful round

## 🎮 Example Gameplay

```
🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯
I'm thinking of a number... Can you guess it?

Choose your difficulty level:
1. Easy - Numbers 1-50 (10 attempts)
2. Medium - Numbers 1-100 (8 attempts)
3. Hard - Numbers 1-200 (6 attempts)
4. Expert - Numbers 1-500 (5 attempts)

Enter difficulty (1-4): 2

🎮 Starting Medium mode!
I'm thinking of a number between 1 and 100
You have 8 attempts. Good luck!

Attempt 1/8 - Enter your guess: 50
📈 Too low! 🧊 Cold
Attempts remaining: 7

Attempt 2/8 - Enter your guess: 75
📉 Too high! 🟡 Warm
Attempts remaining: 6

Attempt 3/8 - Enter your guess: 65
📈 Too low! 🔥 Very Hot!
Attempts remaining: 5

Attempt 4/8 - Enter your guess: 68
🎉 CONGRATULATIONS! 🎉
You guessed 68 in 4 attempts!
Time taken: 23.4 seconds
Your score: 132 points
```

## 🛠️ Code Structure

### Main Class: `NumberGuessingGame`
- **Game State Management**: Tracks statistics and game progress
- **Difficulty Configuration**: Manages different challenge levels
- **Scoring Logic**: Calculates points based on performance
- **User Interface**: Handles display and input/output

### Key Methods
- `play_round()`: Manages a single game session
- `get_hint()`: Provides proximity-based feedback
- `calculate_score()`: Computes final score
- `display_stats()`: Shows performance statistics

## 🎯 Strategy Tips

1. **Start with Binary Search**: For larger ranges, try the middle value first
2. **Use the Hints**: Pay attention to temperature clues for efficient guessing
3. **Choose Your Difficulty**: Balance challenge with achievable goals
4. **Track Patterns**: Learn from your statistics to improve over time
5. **Speed Matters**: Faster completion times show mastery

## 🚀 Future Enhancements

Potential improvements for contributors:
- **Multiplayer Mode**: Compete with friends
- **Leaderboard System**: Global high scores
- **Custom Ranges**: User-defined number ranges
- **Hint Customization**: Adjustable hint sensitivity
- **Game Modes**: Timed challenges, streak modes
- **GUI Version**: Graphical user interface
- **Achievement System**: Unlock rewards for milestones

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the Repository**
2. **Create a Feature Branch**: `git checkout -b feature/AmazingFeature`
3. **Commit Changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to Branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Contribution Ideas
- Add new difficulty levels
- Implement different hint systems
- Create themed number ranges
- Add sound effects (if expanding to GUI)
- Optimize scoring algorithms
- Add data persistence for long-term statistics

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic number guessing games
- Built with Python's built-in libraries for maximum compatibility
- Designed for educational purposes and fun!

## 📞 Support

If you encounter any issues or have suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Feel free to fork and experiment!

---

**Happy Guessing! May the odds be ever in your favor!** 🍀