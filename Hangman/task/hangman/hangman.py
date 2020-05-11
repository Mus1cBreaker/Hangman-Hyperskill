# Write your code here
import random

word_list = 'python', 'java', 'kotlin', 'javascript'
answer = random.choice(word_list)
guessed_letters = set()
input_letters = set()
lives = 0


def print_hint():
    print(''.join([letter if letter in guessed_letters else '-' for letter in answer]))


def try_a_guess(input_letter):
    if len(input_letter) == 1:
        if 123 > ord(input_letter) > 96:
            global lives
            if input_letter in input_letters or input_letter in guessed_letters:
                print("You already typed this letter")
            elif input_letter in answer and input_letter not in guessed_letters:
                guessed_letters.add(input_letter)
            else:
                print("No such letter in the word")
                input_letters.add(input_letter)
                lives += 1
        else:
            print("It is not an ASCII lowercase letter")
    else:
        print("You should print a single letter")


print("H A N G M A N")
start = ""
while start != "exit":
    start = input('Type "play" to play the game, "exit" to quit: ')
    if start == "play":
        while lives < 8 and guessed_letters != set(answer):
            print()
            print_hint()
            try_a_guess(input("Input a letter: "))

        if guessed_letters == set(answer):
            print("You guessed the word!\nYou survived!")
        else:
            print("You are hanged!")
