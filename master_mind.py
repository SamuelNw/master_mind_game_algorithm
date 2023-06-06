"""
Info: A color checker game that takes an input of 4 colors from a user and
checks that input against the computer's own generated code and gives output
of number of colors that match those in the correct code, that in the correct
position, and those in the wrong position.
The user is allowed to guess a maximum of 10 times then if unable to generate
the correct answer after the tenth guess, it is presented to them.
"""

import random

# Constants
COLORS = ["G", "Y", "R", "B", "P", "V", "W", "I", "O", "M"]
CODE_LENGTH = 4
TRIES = 10


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))

    return code


def get_user_guess():

    while True:
        guess = input(
            f"Input your guess ({CODE_LENGTH} letters separated by a space): ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"Your guess must be {CODE_LENGTH} letters long.")
            continue

        for char in guess:
            if char not in COLORS:
                print(f"{char} not in the choices. Try again.")
                break

        else:
            break

    return guess


def check_code(user_code, generated_code):
    color_counts = {}
    correct_pos, incorrect_pos = 0, 0

    for color in generated_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for user_color, generated_color in zip(user_code, generated_code):
        if user_color == generated_color:
            correct_pos += 1
            print(f"{user_color} in correct pos")
            color_counts[user_color] -= 1

    for user_color, generated_color in zip(user_code, generated_code):
        if user_color in color_counts and color_counts[user_color] > 0:
            incorrect_pos += 1
            print(f"{user_color} in wrong pos")
            color_counts[user_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(
        f"Welcome to mastermind. You have {TRIES} tries to get the correct answer. Goodluck...")
    print("The valid colors are: ", " ".join(x for x in COLORS))
    real_code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = get_user_guess()
        correct_pos, incorrect_pos = check_code(guess, real_code)

        if correct_pos == CODE_LENGTH:
            print(f"You won! You did it in {attempts} attempts. Congrats!!!")
            print(f"The correct answer: ", " ".join(x for x in guess))
            break

        print(
            f"Correct Positions {correct_pos} | Incorrect Positions {incorrect_pos}.")

    else:
        print(f"You ran out of chances. The correct answer was: ",
              " ".join(x for x in real_code))


if __name__ == "__main__":
    game()
