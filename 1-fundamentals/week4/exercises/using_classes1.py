#!/usr/bin/python3

class Player():
    """Defining a Player class"""

    def __init__(self, name, hp):
        """Declare and Initialize instance attributes"""
        self.name = name  # Attribute
        self.hp = hp  # Attribute
        self.score = 0  # Added in attribute, default value


player1 = Player("Ash", 1200)
player2 = Player("bash", 1400)

print("P1:", player1.name, "--HP:", player1.hp, "--SCORE:", player1.score)
print("P2:", player2.name, "--HP:", player2.hp, "--SCORE:", player2.score)

player1.hp += 500 
player1.score += 10

print(f"P1:, {player1.name}, HP: {player1.hp}, SCORE: {player1.score}")
print(f"P2:, {player2.name}, HP: {player2.hp}, SCORE: {player2.score}")

