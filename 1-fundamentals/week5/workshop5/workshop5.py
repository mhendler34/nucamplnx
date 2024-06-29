#!/usr/bin/python3

import random


def guess_random_number(tries, start, stop):
    """Function to guess random number"""
    random_int = random.randint(start, stop)
    numbers_guessed = []  # list to hold guessed numbers

    while tries != 0:
        print(f"Guess a number between {start} and {stop}")
        print(f"Number of tries remaining: {tries}")
        guess = int(input('> '))

        # Validate number is within parameters
        if guess < start or guess > stop:
            print(f"Please enter an integer between {start} and {stop}\n")
        elif guess not in numbers_guessed:  # new guess
            if guess == random_int:
                print("<< CORRECT >>")
                return
            elif guess < random_int:
                print("^^ Guess HIGHER ^^\n")
            else:
                print("vv Guess LOWER vv\n")
            numbers_guessed.append(guess)  # added guess to list
            tries -= 1
        else:
            print("Number already used, pick again please\n")
    print("Sorry, you did not guess the number.")
    print(f"The random number was: {random_int}")


# guess_random_number(5, 0, 10)


def guess_random_num_linear(tries, start, stop):
    """Function to guess random number with linear search algorithm"""
    print("Linear Search Algorithm will guess the random number!")
    random_int = random.randint(start, stop)  # these are integers
    print(f"The random number to guess is {random_int}\n")
    for x in range(0, 11):  # these are integers
        print(f"Linear search attempts remaining: {tries}")
        if tries == 0:
            print("The computer ran out of guesses")
            print(f"The random number was {random_int}")
            return -1
        print(f"Computer guesses... {x}")
        if x == random_int:
            print("<< CORRECT >>")
            return
        elif x < random_int:
            print("^^ HIGHER ^^\n")
        elif x > random_int:
            print("vv LOWER vv\n")
        tries -= 1


# guess_random_num_linear(5, 0, 10)


def guess_random_num_binary(tries, start, stop):
    """Function to use binary search algorithm to guess random number"""
    print("Binary Search Algorithm will guess the random number")
    random_int = random.randint(0, 100)
    print(f"The random number to guess is: {random_int}\n")

    lower_bound = start
    upper_bound = stop
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        print(f"pivot is: {pivot}")
        print(f"Number of attempts remaining: {tries}")
        if tries == 0:
            print("Did not get there in time. Out of guess attempts")
            return -1

        if pivot == random_int:
            print(f"SUCCESS! {pivot}")
            return pivot
        if pivot > random_int:
            upper_bound = pivot + 1
            print("Go lower\n")
        else:
            lower_bound = pivot - 1
            print("Go higher\n")
        tries -= 1


# guess_random_num_binary(5, 0, 100)


def userchoice_guess_random_number():
    """Function to let user input parameters and choose what type of search"""
    print("First, choose game parameters. Second, choose how to play.")
    tries = int(input("Enter number of attempts to guess the number: "))
    start = int(input("Enter the number at the start of the range: "))
    stop = int(input("Enter the number at the end of the number range: "))
    print("Option 1: user guesses the random number")
    print("Option 2: computer guesses using linear search algorithm")
    print("Option 3: computer guesses using binary search algorithm")
    response = input("Enter the number of the option you would like")
    if response == '1':
        guess_random_number(tries, start, stop)
    elif response == '2':
        guess_random_num_linear(tries, start, stop)
    elif response == '3':
        guess_random_num_binary(tries, start, stop)
    else:
        print("Maybe some other time")


userchoice_guess_random_number()

