from random import randint
from re import split
from colorama import init

# Import words
with open("words.txt") as f:
    words = split(r"\s+", f.read())

class Result:
    GREY = 0
    YELLOW = 1
    GREEN = 2

    # Returns all grey letters
    def redundant_letters(self):
        return [x[0] for x in self.res if x[1] == Result.GREY]

    # Checks if all letters are green (win condition)
    def is_win(self):
        for x in self.res:
            color = x[1]
            if color != Result.GREEN:
                return False
        return True

    # These are obvious

    def __str__(self):
        string = ""
        for x in self.res:
            letter, color = x
            if color == Result.GREEN:
                string += "\033[32m" + letter + "\033[m"
            elif color == Result.YELLOW:
                string += "\033[33m" + letter + "\033[m"
            else:
                string += letter
        return string

    def __init__(self, guess, answer):
        self.res = []
        if len(guess) != len(answer):
            raise ValueError
        for i in range(len(guess)):
            color = Result.GREY
            if guess[i] == answer[i]:
                color = Result.GREEN
            elif guess[i] in answer:
                color = Result.YELLOW
            self.res.append((guess[i], color))

# Game

init()

print("wordle game")
print("\033[32mgreen\033[m = Correct letter, correct position")
print("\033[33myellow\033[m = Correct letter, incorrect postition")
print()

while True:
    # Initialize answer and letters
    answer = words[randint(0, len(words) - 1)]
    letters = [chr(i) for i in range(97, 123)]
    # Main loop
    while True:
        print("\033[91mLetters: " + " ".join(letters) + "\033[m")
        guess = input("> ")
        result = Result(guess, answer)
        letters = [x for x in letters if x not in result.redundant_letters()]
        print(result)
        if result.is_win():
            print("You won the game!")
            break
    while True:
        play_again = input("Play again?(y/n) ").lower()
        if play_again == "y" or play_again == "n":
            break
    if play_again == "n":
        break
