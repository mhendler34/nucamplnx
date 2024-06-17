#!/usr/bin/python3
# Week1 - Battlegame

# DECLARE
wizard = 'Wizard'
elf = 'Elf'
human = 'Human'
magi = 'Magi'

wizard_hp = 70
elf_hp = 100
human_hp = 150
magi_hp = 200
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
magi_damage = 200
dragon_damage = 50

# INPUT
while True:  # Run loop until user picks 1, 2, 3
    print("Welcome to the Battlegame!")
    print("1)   Wizard")
    print("2)   Elf")
    print("3)   Human")
    print("4)   Magi")
    print("Type 'x' to exit")

    character = input("Please choose your character: ").title()

    if character == 'X':
        break
    try:  # Value error @ int(character) entering 'elf' in prompt
        if character == 'Wizard' or int(character) == 1:
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            print(f"You have chosen the {character}!")
            print(f"Health: {my_hp}")
            print(f"Damage: {my_damage}")
            break
    except ValueError:
        pass

    try:  # Value error @ int(character) when entering 'elf' in prompt
        if character == 'Elf' or int(character) == 2:
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            print(f"You have chosen the {character}!")
            print(f"Health: {my_hp}")
            print(f"Damage: {my_damage}")
            break
    except ValueError:
        pass

    try:  # Value error @ int(character) when entering 'elf' in prompt
        if character == 'Human' or int(character) == 3:
            character = human
            my_hp = human_hp
            my_damage = human_damage
            print(f"You have chosen the {character}!")
            print(f"Health: {my_hp}")
            print(f"Damage: {my_damage}")
            break
    except ValueError:
        pass

    if character == 'Magi' or int(character) == 4:
        character = magi
        my_hp = magi_hp
        my_damage = magi_damage
        print(f"You have chosen the {character}")
        print(f"Health: {my_hp}")
        print(f"Damage: {my_damage}")
        break
    else:
        print("Please enter valid number or character")

# Second While Loop

while True:  # Run loop until dragon health is <= ZERO

    if character == 'X':
        print("Thank you for playing")
        break

    dragon_hp = dragon_hp - my_damage
    print(f"\nThe {character} has damaged the Dragon!")
    print(f"The Dragon's hitpoints are now: {dragon_hp}")
    if dragon_hp <= 0:
        print("\nThe Dragon has lost the battle.")
        break

    my_hp = my_hp - dragon_damage
    print(f"\nThe Dragon strikes back at the {character}!")
    print(f"The {character} hitpoints are: {my_hp}")
    if my_hp <= 0:
        print(f"\nThe {character} has lost the battle.")
        break











