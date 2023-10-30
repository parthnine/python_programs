from guizero import App, Box, Text, TextBox, PushButton
import random

class GuessTheNumberGame:
    def __init__(self):
        self.app = App("Guess the Number Game")
        self.game_box = Box(self.app, layout="grid", align="top")
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        
        # print(self.target_number)
        self.message = Text(self.game_box, text="Guess a number between 1 and 100:", grid=[0, 0, 2, 1])
        self.guess_input = TextBox(self.game_box, width=20, grid=[0, 1])
        self.submit_button = PushButton(self.game_box, text="Submit", command=self.check_guess, grid=[1, 1])
        self.result_text = Text(self.game_box, text="", grid=[0, 2, 2, 1])
        
    def check_guess(self):
        self.attempts += 1
        guess = int(self.guess_input.value)
        
        if guess < self.target_number:
            self.result_text.value = "Try a higher number."
        elif guess > self.target_number:
            self.result_text.value = "Try a lower number."
        else:
            self.result_text.value = f"Congratulations! You guessed the number {self.target_number} in {self.attempts} attempts."
            self.submit_button.disable()
        
game = GuessTheNumberGame()
game.app.display()