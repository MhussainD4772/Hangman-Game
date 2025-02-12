# 🎮 Hangman Game

## **📚 Overview**
Hangman is a classic word-guessing game where players try to guess a hidden word one letter at a time. If they guess incorrectly too many times, they lose!

## **🚀 Features**
- ✅ Random word selection from a predefined list
- ✅ ASCII art for Hangman stages
- ✅ Lives system with a limited number of incorrect guesses
- ✅ Keeps track of correctly guessed letters
- ✅ Displays progress after each guess

## **🛠️ Installation**
1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/Hangman-Game.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Hangman-Game
   ```
3. **Run the game:**
   ```bash
   python hangman_game.py
   ```

## **🐂 Project Structure**
```
Hangman-Game/
│── hangman_game.py        # Main game logic
│── hangman_words.py       # Word list for the game
│── hangman_art.py         # ASCII art for hangman stages
│── README.md              # Project documentation
```

## **🖥️ How to Play**
1. Run `hangman_game.py`.
2. A random word will be chosen, displayed as `_ _ _ _ _` (hidden format).
3. Guess a letter:
   - **Correct guess** → The letter is revealed.
   - **Incorrect guess** → You lose a life, and the hangman drawing progresses.
4. Keep guessing until:
   - 🎉 **You win!** (all letters are guessed)
   - 💀 **You lose!** (all lives are gone)

## **🛠️ Future Improvements**
- 🔹 Add difficulty levels (easy, medium, hard)
- 🔹 Allow users to enter custom word lists
- 🔹 Implement a GUI version using Tkinter
- 🔹 Fetch words dynamically from an API

## **📝 License**
This project is open-source and available under the **MIT License**.

## **👨‍💻 Author**
- **Syed Mohammed Hussain** - [GitHub Profile](https://github.com/MhussainD4772)

