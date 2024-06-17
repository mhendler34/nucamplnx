#!/usr/bin/python3

import random

diamonds = ['AD', '2D', '3D', '4D', '5D', '6D',
            '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD']

hand = []

while diamonds:  # While diamonds list is has entries
    print("Press enter to pick a card or 'q' to quit")
    response = input('> ').lower()

    if response == 'q':
        break
    elif response != 'q':
        card = random.choice(diamonds)
        if card in diamonds:
            diamonds.remove(card)
            hand.append(card)
            print(f"Your Hand: {hand}")
            print(f"Remaining cards: {diamonds}")
            if not diamonds:
                print("There are no more cards left to pick")

