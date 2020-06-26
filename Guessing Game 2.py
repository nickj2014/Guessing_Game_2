import random


def main():
    lowest, highest, counter = 0, 101, 1  # Initial guess range and value for if guess is first try
    run = True
    guess = random.randrange(lowest, highest)  # First guess
    print("""Welcome to the guessing game, think of a number between 0-100!
    Enter 'Correct', 'Higher' or 'Lower' to generate a new guess!""")

    while run:
        print(f"I guess {guess}.")  # Print guess, receive input
        check = input("Correct, higher or lower? ")

        if check.lower() == "correct":  # If correct, print counter and exit
            print(f"I won? How exciting. It took me {counter} attempts.")
            run = False

        elif check.lower() == "higher":  # Check higher option
            lowest = guess + 1  # Lowest value now guess + 1 so can't guess that value again
            if not found(lowest, highest, counter):  # If found returns false, new guess
                guess = random.randrange(lowest, highest)
                counter += 1
            else:  # If found returns true, end game
                run = False

        elif check.lower() == "lower":
            highest = guess - 1
            if not found(lowest, highest, counter):
                guess = random.randrange(lowest, highest)
                counter += 1
            else:
                run = False


def found(low, high, counter):
    if low == high:  # If lowest = highest, no more numbers to guess so must be correct
        counter += 1
        print(f"It must be {low} then! It took me {counter} attempts.")
        return True
    else:
        return False


main()
