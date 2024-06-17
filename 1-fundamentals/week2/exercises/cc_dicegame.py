#!/usr/bin/python3

import random


def dice_game():
    """Function for dice game"""
    # Initialize Variables
    high_score = 0
    total_score = 0
    roll = 0
    while True:
        print(f"Current High Score: {high_score}")
        print("1)   Roll Dice")
        print("2)   Leave Game")
        print("Enter your choice (1 or 2): ")

        response = int(input('> '))
        if response == 1:
            # ROLL 1
            total_score = 0
            roll = random.randint(1, 6)
            print(f"You rolled a... {roll}")
            total_score += roll
            # ROLL 2
            roll = random.randint(1, 6)
            print(f"You rolled a... {roll}")
            total_score += roll
            print(f"\nYour total score is {total_score}")
            
            if total_score > high_score:
                high_score = total_score
                print(f"\nYou rolled a new high score! {high_score}\n")
        else:
            print("Goodbye!")
            break


dice_game()  # Calling function dice_game
