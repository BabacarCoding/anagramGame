import csv
import random

# Generating word section
file = open("words.csv", "r")
csv_reader = csv.reader(file)

word_list = []
for row in csv_reader:
    word_list.append(row)


def anagram():

    word = random.choice(word_list)
    word = ("".join(map(str, word))).lower()
    original_word = word

    # Scrambling word
    list_word = list(word)
    random.shuffle(list_word)
    word = "".join(map(str, list_word))

    print(f"\n \n{word} is the word you must guess. It is scrambled, and you have five tries to guess the correct orientation. \n")

    win = 0
    tries = 5
    print(f"What do you think the word {word} is?")

    while tries > 0:
        tries -= 1
        print("")
        choice = input("")
        print("")

    # if else to check if guess == word
        if choice == original_word:
            win = 1
            tries = 0
        else:
            print(f"{choice} is not the word. You have {tries} tries left.")

    # mechanism for checking win
    if win == 1:
        print(f"Good job guessing the word {choice} in under five tries!\n")
    else:
        print(f"\nYou failed. The correct word is {original_word}.\n")


anagram()
