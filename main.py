import tkinter as tk
import random

# ------------------------------
# ✅ Word List
# ------------------------------
word_list = ["python", "developer", "hangman", "coding", "project", "interface"]

# ------------------------------
# ✅ ASCII Hangman Stages (for GUI)
# ------------------------------
stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]

# ------------------------------
# ✅ Game Variables
# ------------------------------
chosen_word = ""
display_word = ""
correct_guesses = set()
lives = 6

# ------------------------------
# ✅ GUI Setup
# ------------------------------
root = tk.Tk()
root.title("Tkinter Hangman")
root.geometry("1200x700")
root.configure(bg="#222")  # Dark background

# 🎨 Title Label
title_label = tk.Label(root, text="HANGMAN", font=("Arial", 28, "bold"), fg="white", bg="#222")
title_label.pack(pady=10)

# 🎭 ASCII Art Hangman
hangman_label = tk.Label(root, text=stages[lives], font=("Consolas", 14), fg="red", bg="#222")
hangman_label.pack()

# 🏆 Word Display
word_label = tk.Label(root, text="", font=("Arial", 24, "bold"), fg="yellow", bg="#222")
word_label.pack(pady=10)

# ❤️ Lives Counter
lives_label = tk.Label(root, text=f"Lives: {lives}/6", font=("Arial", 16, "bold"), fg="white", bg="#222")
lives_label.pack()

# 🔠 Guess Entry
guess_entry = tk.Entry(root, font=("Arial", 18), width=5, justify="center")
guess_entry.pack(pady=10)

# 📝 Status Message
status_label = tk.Label(root, text="Guess a letter!", font=("Arial", 14), fg="white", bg="#222")
status_label.pack()


# ------------------------------
# ✅ Functions
# ------------------------------
def start_game():
    """Initialize a new game."""
    global chosen_word, display_word, correct_guesses, lives

    chosen_word = random.choice(word_list)
    display_word = "_" * len(chosen_word)
    correct_guesses = set()
    lives = 6

    update_ui("New game started!")


def update_ui(message=""):
    """Update the GUI with the current game state."""
    spaced_word = " ".join([char if char in correct_guesses else "_" for char in chosen_word])
    word_label.config(text=spaced_word)
    hangman_label.config(text=stages[6 - lives])
    lives_label.config(text=f"Lives: {lives}/6")
    status_label.config(text=message)


def check_guess():
    """Process a guessed letter."""
    global lives

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if not guess or len(guess) > 1 or not guess.isalpha():
        update_ui("Enter a single valid letter.")
        return

    if guess in correct_guesses:
        update_ui(f"You already guessed '{guess}'.")
        return

    correct_guesses.add(guess)

    if guess in chosen_word:
        update_ui(f"Good guess! '{guess}' is in the word.")
    else:
        lives -= 1
        update_ui(f"'{guess}' is NOT in the word! Lives lost.")

    # Win/Loss Check
    if "_" not in " ".join([char if char in correct_guesses else "_" for char in chosen_word]):
        update_ui("🎉 YOU WIN! 🎉")
        guess_entry.config(state=tk.DISABLED)
    elif lives == 0:
        update_ui(f"💀 YOU LOSE! The word was '{chosen_word}'")
        guess_entry.config(state=tk.DISABLED)


def restart_game():
    """Restart the game."""
    guess_entry.config(state=tk.NORMAL)
    start_game()


# ------------------------------
# ✅ Buttons
# ------------------------------
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=check_guess, bg="green", fg="white")
submit_button.pack(pady=5)

restart_button = tk.Button(root, text="Restart", font=("Arial", 14), command=restart_game, bg="blue", fg="white")
restart_button.pack(pady=5)

# ------------------------------
# ✅ Start the Game
# ------------------------------
start_game()
root.mainloop()



