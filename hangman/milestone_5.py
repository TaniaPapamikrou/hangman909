import random

class Hangman:
    def __init__(self, word_list, mum_lives = 5):
        self.word_list = word_list
        self.mum_lives = mum_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len([letter for letter in set(self.word) if letter not in self.word_guessed])
        self.list_of_guesses = []

    def check_guess(self, letter):
        letter = letter.lower()
        if letter in self.word:
            print(f"Good guess! {letter} is in the word")
            letter_index = 0
            for position, char in enumerate(self.word):
                if char == letter:
                    letter_index = position
                    self.word_guessed[letter_index] = letter
                    print(f"Nice! {letter} is in the word!")
                    print(f"{self.word_guessed}")
                    self.num_letters -= 1
                else:
                    self.num_lives -= 1
                    print(f"Sorry, {letter} is not in the word.")
        print(f"{self.list_visual[self.num_lives]}")
        print(f"You have {self.num_lives} lives left.")
        self.list_letters.append(letter)

def ask_for_input(self):
    while True:
        guess = input("Choose a single letter: ")
        if len(guess) != 1 and not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif letter in self.list_letters:
            print(f"You already tried {letter} letter")
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num.lives == 0:
            print("You lost!")
            break
        elif game.num_lives > 0:
            game.ask_for_input()
        else:
            print("Congratulations, you won the game!")
            break
