from random import choice
from colorama import Fore, Back, Style
from time import sleep

possibilities_dict = {"r": "Rock", "p": "Paper", "s": "Scissors",
                      "rock": "Rock", "paper": "Paper", "scissors": "Scissors",
                      "1": "Rock", "2": "Paper", "3": "Scissors"}
possibilities_comp = ["r", "p", "s"]
possibilities_rock = ["rock", "r", "1"]
possibilities_paper = ["paper", "p", "2"]
possibilities_scissors = ["scissors", "s", "3"]

def main():
    score_player, score_comp = 0, 0
    print(Back.LIGHTBLACK_EX, end="")
    print("Score 10 before computer to win!\nEnter zxc to exit the game")
    print(Style.RESET_ALL, end="")
    reply = ""
    winner_exists = False
    while score_player < 10 or score_comp < 10:
        print(Fore.CYAN, end="")
        print("Rock? Paper? Scissors?")
        print(Fore.MAGENTA, end="")
        reply = input("Enter you choice: ").lower()
        com_guess = choice(possibilities_comp)
        print(Style.RESET_ALL, end="")
        if reply in possibilities_rock:
            if com_guess in possibilities_rock:
                tie_case(reply, com_guess)
            elif com_guess in possibilities_paper:
                l_case(reply, com_guess)
                score_comp += 1
            elif com_guess in possibilities_scissors:
                w_case(reply, com_guess)
                score_player += 1

        elif reply in possibilities_paper:
            if com_guess in possibilities_rock:
                w_case(reply, com_guess)
                score_player += 1
            elif com_guess in possibilities_paper:
                tie_case(reply, com_guess)

            elif com_guess in possibilities_scissors:
                l_case(reply, com_guess)
                score_comp += 1

        elif reply in possibilities_scissors:
            if com_guess in possibilities_rock:
                l_case(reply, com_guess)
                score_comp += 1

            elif com_guess in possibilities_paper:
                w_case(reply, com_guess)
                score_player += 1
            elif com_guess in possibilities_scissors:
                tie_case(reply, com_guess)

        elif reply == "zxc" or score_player < 10 or score_comp < 10:
            winner_exists == True
            break

        elif reply == "score":
            print(f"Player score: {score_player}\nComputer score: {score_comp}\n")

        else:
            print(Style.RESET_ALL, end="")
            print("Enter a valid choice!\n")

    if winner_exists: print("You won" if (score_com < score_player) else "Computer won")


def tie_case(r, c):
    print(Back.BLACK, end="")
    print(f"Computer picked: {possibilities_dict[c]}")
    print(Style.RESET_ALL, end="")
    print(Fore.LIGHTYELLOW_EX, end="")
    sleep(1)
    print(f"Tie! Both picked {possibilities_dict[r]}\n")


def w_case(r, c):
    print(Back.BLACK, end="")
    print(f"Computer picked: {possibilities_dict[c]}")
    print(Style.RESET_ALL, end="")
    print(Fore.GREEN, end="")
    sleep(1)
    print(f"You won! {possibilities_dict[r]} beats {possibilities_dict[c]}\n")


def l_case(r, c):
    print(Back.LIGHTBLACK_EX, end="")
    print(f"Computer picked: {possibilities_dict[c]}")
    print(Style.RESET_ALL, end="")
    print(Fore.RED, end="")
    sleep(1)
    print(f"You lost! {possibilities_dict[r]} looses to {possibilities_dict[c]}\n")


if __name__ == '__main__':
    main()
