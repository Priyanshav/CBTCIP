import tkinter as tk
from tkinter import simpledialog, messagebox


class MastermindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind Game")

        self.secret_number = ""
        self.length = 0
        self.p1_attempts = 0
        self.p2_attempts = 0

        self.label = tk.Label(root, text="Welcome to Mastermind!")
        self.label.grid(padx=50, pady=10)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.grid(padx=50, pady=10)

    def start_game(self):
        self.label.config(text="Player1, set a multi-digit number:")
        self.secret_number = simpledialog.askstring("Input", "Player 1's number:", show="*")
        self.length = len(self.secret_number)

        self.label.config(text="Player 2,guess the number!")
        self.p2_attempts = 0
        self.p2_guess()

    def p2_guess(self):
        while True:
            guess = simpledialog.askstring("Input", f"Enter your {self.length}-digit guess:")
            if len(guess) == self.length and guess.isdigit():
                self.p2_attempts += 1
                if guess == self.secret_number:
                    messagebox.showinfo("Result", f"Congratulations Player 2! You guessed the number in {self.p2_attempts} tries.")
                    self.switch_roles()
                    break
                else:
                    correct_positions = self.get_feedback(self.secret_number,guess)
                    messagebox.showinfo("Feedback", f"{correct_positions} digit(s) are correct and in the correct position.")
            else:
                messagebox.showerror("Error", f"Invalid input. Please enter exactly {self.length} digits.")

    def switch_roles(self):
        self.label.config(text="Player 2, set a multi-digit number:")
        self.secret_number = simpledialog.askstring("Input", "Player 2's number:", show="*")
        self.length = len(self.secret_number)

        self.label.config(text="Player 1,guess the number!")
        self.p1_attempts = 0
        self.p1_guess()

    def p1_guess(self):
        while True:
            guess = simpledialog.askstring("Input", f"Enter your {self.length}-digit guess:")
            if len(guess) == self.length and guess.isdigit():
                self.p1_attempts += 1
                if guess == self.secret_number:
                    messagebox.showinfo("Result", f"Congratulations Player 1! You guessed the number in {self.p1_attempts} tries.")
                    self.determine_winner()
                    break
                else:
                    correct_positions = self.get_feedback(self.secret_number,guess)
                    messagebox.showinfo("Feedback", f"{correct_positions} digits are correct and in the correct position.")
            else:
                messagebox.showerror("Error", f"Invalid input. Please enter exactly {self.length} digits.")

    def determine_winner(self):
        if self.p1_attempts > self.p2_attempts:
            messagebox.showinfo("Winner", "Player 2 wins the game!")
        elif self.p1_attempts < self.p2_attempts:
            messagebox.showinfo("Winner", "Player 1 wins the game!")
        else:
            messagebox.showinfo("No Winner", "The match tied!")

    def get_feedback(self, secret, guess):
        return sum(s == g for s, g in zip(secret, guess))


if __name__ == "__main__":
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()
