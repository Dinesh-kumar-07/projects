'''
Project Name : Hangman_game
designed by  : Dinesh Kumar G
designed on  : 28.06.2025 , 11.00am
purpose      : creating a simple and creative game in python
'''
import tkinter as tk
from tkinter import messagebox
import random

# 50 words with hints
word_list = [
    ("apple", "A common red or green fruit"),
    ("banana", "A long yellow fruit"),
    ("cherry", "A small red fruit with a pit"),
    ("grapes", "Small round fruit in bunches"),
    ("orange", "A citrus fruit rich in vitamin C"),
    ("mango", "Sweet tropical fruit with a large seed"),
    ("peach", "A fuzzy fruit with a stone"),
    ("lemon", "A sour yellow citrus fruit"),
    ("carrot", "An orange root vegetable"),
    ("potato", "Brown skin vegetable used for fries"),
    ("tiger", "A large striped wild cat"),
    ("lion", "King of the jungle"),
    ("elephant", "Largest land animal"),
    ("zebra", "Striped horse-like animal"),
    ("giraffe", "Tallest land animal"),
    ("dog", "Man’s best friend"),
    ("cat", "Purrs and chases mice"),
    ("mouse", "A small rodent"),
    ("rabbit", "Hops and loves carrots"),
    ("horse", "Used for riding or racing"),
    ("cloud", "Fluffy thing in the sky"),
    ("rain", "Falls from clouds"),
    ("sun", "The star that lights our world"),
    ("moon", "Orbits the Earth"),
    ("star", "Twinkles in the night sky"),
    ("river", "Flows into lakes or oceans"),
    ("mountain", "Very high land"),
    ("desert", "Dry place with little rain"),
    ("ocean", "Biggest water body"),
    ("island", "Land surrounded by water"),
    ("school", "Place for learning"),
    ("teacher", "Helps you learn"),
    ("pencil", "Used for writing"),
    ("book", "Pages with stories or info"),
    ("chair", "Used for sitting"),
    ("table", "Used for eating or working"),
    ("window", "Glass part of a wall"),
    ("door", "You open it to enter"),
    ("house", "Place where people live"),
    ("car", "Used to drive on roads"),
    ("bicycle", "Two wheels, no engine"),
    ("train", "Moves on tracks"),
    ("bus", "Carries many people"),
    ("plane", "Flies in the sky"),
    ("boat", "Floats on water"),
    ("phone", "Used to call or text"),
    ("watch", "Worn on wrist to tell time"),
    ("clock", "Hangs on wall, tells time"),
    ("shirt", "Worn on upper body"),
    ("shoes", "Worn on feet"),
]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.setup_game()

    def setup_game(self):
        self.word, self.hint = random.choice(word_list)
        self.word_display = ["_" for _ in self.word]
        self.guesses_left = 6
        self.guessed_letters = []

        self.hint_label = tk.Label(self.root, text=f"Hint: {self.hint}", font=("Arial", 12))
        self.hint_label.pack(pady=10)

        self.word_label = tk.Label(self.root, text=" ".join(self.word_display), font=("Arial", 24))
        self.word_label.pack(pady=10)

        self.guesses_label = tk.Label(self.root, text=f"Guesses left: {self.guesses_left}", font=("Arial", 12))
        self.guesses_label.pack(pady=5)

        self.guessed_label = tk.Label(self.root, text="Guessed letters: None", font=("Arial", 10))
        self.guessed_label.pack(pady=5)

        self.entry = tk.Entry(self.root, font=("Arial", 14), width=5, justify='center')
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.restart_game)
        self.play_again_button.pack(pady=10)
        self.play_again_button.config(state="disabled")

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showwarning("Invalid input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already guessed", "You've already guessed that letter.")
            return

        self.guessed_letters.append(guess)
        self.guessed_label.config(text=f"Guessed letters: {', '.join(self.guessed_letters)}")

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_display[i] = guess
            self.word_label.config(text=" ".join(self.word_display))
        else:
            self.guesses_left -= 1
            self.guesses_label.config(text=f"Guesses left: {self.guesses_left}")

        self.check_game_status()

    def check_game_status(self):
        if "_" not in self.word_display:
            messagebox.showinfo("You Win!", f"Congratulations! You guessed the word: {self.word}")
            self.end_game()
        elif self.guesses_left == 0:
            messagebox.showinfo("Game Over", f"You're out of guesses! The word was: {self.word}")
            self.end_game()

    def end_game(self):
        self.guess_button.config(state="disabled")
        self.play_again_button.config(state="normal")

    def restart_game(self):
        self.guess_button.config(state="normal")
        self.play_again_button.config(state="disabled")
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
