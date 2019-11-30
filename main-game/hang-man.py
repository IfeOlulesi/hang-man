# Hangman game(Text edition)
import random
import os


def list_creator(folder, docname):
    docs = os.path.join(folder, docname)

    with open(docs, "r") as f:
        words1 = (f.read().split("\n"))
        return words1


def hangman():

    words = list_creator("Levels", "level-4.txt")

    x = random.randint(0, len(words))
    word = words[x]
    wrong = 0
    stages = [
        "",
        "_______________             ",
        " |           |              ",
        " |           |              ",
        " |           O              ",
        " |         / | \            ",
        " |          / \             ",
        " |                          ",
        " |__________________________",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1

        print(("".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))

        if "_" not in board:
            print("You win!!")
            print("".join(board))
            # so here i should add the level up function

            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}".format(word))

    repeat = input("Would you like to play again? (y/n) ")
    if repeat == "y":
        hangman()
    else:
        print("See you later!!")


hangman()
