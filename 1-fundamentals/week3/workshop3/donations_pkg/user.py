#!/usr/bin/python3

def login(database, username, password):
    """Login Functionality in app"""
    if username in database and password == database[username]:
        print(f"\nWelcome back, {username.title()}!\n")
        return username
    elif username in database and password != database[username]:
        print("\nIncorrect Password, try again\n")
    elif username not in database:
        print("\nUser not found. Please register.\n")


def register(database, username, password):
    """Registration Functionality in app"""
    if len(username) > 10:  # Catch usernames which are too long
        print("\nUsername must be less than 10 characters\n")
        #  Should Return None
    if len(password) < 5:  # Catch password which are too short
        print("\nPassword must be greater than 5 characters\n")
        #  Should return None
    elif username in database:  # If true
        print("\nUsername already registered")
    elif username not in database and len(username) < 10:  # If true
        print(f"\n{username.title()} has been registered\n")
        return username
