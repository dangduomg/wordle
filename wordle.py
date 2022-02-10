from random import randint
from re import split
from colorama import init

data_file = open("words.txt", "r")
data = data_file.read()
data_file.close()

class Result:
    def redundant_letters(self):
        return [x[0] for x in self.res if x[1] == 0]

    def is_win(self):
        for x in self.res:
            color = x[1]
            if color != 2:
                return False
        return True

    def __str__(self):
        string = ""
        for x in self.res:
            letter, color = x
            if color == 2:
                string += "\033[32m" + letter + "\033[m"
            elif color == 1:
                string += "\033[33m" + letter + "\033[m"
            else:
                string += letter
        return string

    def __init__(self, guess, answer):
        self.res = []
        if len(guess) != len(answer):
            raise ValueError
        for i in range(len(guess)):
            color = 0
            if guess[i] == answer[i]:
                color = 2
            elif guess[i] in answer:
                color = 1
            self.res.append((guess[i], color))

# game

init()

print("wordle game")
print("\033[32mgreen\033[m = correct letter, correct position")
print("\033[33myellow\033[m = correct letter, incorrect postition")
print()

while True:        
    words = split(r"\s+", data)
    answer = words[randint(0, len(words) - 1)]
    letters = [chr(i) for i in range(97, 123)]
    while True:
        print("\033[91mletters: " + " ".join(letters) + "\033[m")
        guess = input("> ")
        result = Result(guess, answer)
        letters = [x for x in letters if x not in result.redundant_letters()]
        print(result)
        if result.is_win():
            print("you won the game!")
            break
    play_again = input("play again?(y/n) ")
    if play_again != "y":
        break
