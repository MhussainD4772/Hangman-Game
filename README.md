# 🎮 Hangman Game (Tkinter Version)

## **📚 Overview**
Hangman is a classic word-guessing game where players try to guess a hidden word one letter at a time. If they guess incorrectly too many times, they lose!

This version of Hangman is built using **Tkinter**, providing a graphical user interface (GUI) instead of a text-based console.

## **🚀 Features**
- ✅ **GUI-based Hangman using Tkinter**
- ✅ **Dark mode UI with smooth fonts & animations**
- ✅ **ASCII art for Hangman stages inside the GUI**
- ✅ **Automatic win/loss detection**
- ✅ **Restart button to play again**
- ✅ **Handles repeated guesses & incorrect inputs gracefully**

## **🛠️ Installation**
### **1. Clone this repository:**
```bash
git clone https://github.com/yourusername/Hangman-Game.git
```
### **2. Navigate to the project directory:**
```bash
cd Hangman-Game
```
### **3. Install dependencies:**
```bash
pip install tk
```
*(Tkinter comes pre-installed with Python, but this ensures it’s available.)*

### **4. Run the game:**
```bash
python main.py
```

## **🐂 Project Structure**
```
Hangman-Game/
|── main.py               # GUI-based Hangman game (Tkinter)
|── README.md             # Project documentation
```

## **🖥️ How to Play**
1. Run `main.py`.
2. A random word will be chosen, displayed as `_ _ _ _ _` (hidden format).
3. Guess a letter:
   - **Correct guess** → The letter is revealed.
   - **Incorrect guess** → You lose a life, and the Hangman ASCII art updates.
4. Keep guessing until:
   - 🎉 **You win!** (all letters are guessed)
   - 💀 **You lose!** (all lives are gone)

## **🛠️ Future Improvements**
- 🔹 Add difficulty levels (easy, medium, hard)
- 🔹 Allow users to enter custom word lists
- 🔹 Implement sound effects for correct/wrong guesses
- 🔹 Improve animations & UI effects
- 🔹 Add a leaderboard with scores

## **📝 License**
This project is open-source and available under the **MIT License**.

## **👨‍💻 Author**
- **Syed Mohammed Hussain** - [GitHub Profile](https://github.com/MhussainD4772)



