#!/usr/bin/python3

def show_balance(balance):
    """Function to show bank account balance"""
    print(f"Your current balance is ${balance}.")


def deposit(balance):
    """Function to handle deposit amounts"""
    deposit_amount = input("Enter amount to deposit: ")
    total_balance = int(balance) + int(deposit_amount)
    return total_balance


def withdraw(balance):
    """Function to handle withdraw amounts"""
    withdraw_amount = input("Enter amount to withdraw: ")
    total_balance = int(balance) - int(withdraw_amount)
    return total_balance


def logout(name):
    """Function handles logging out"""
    print(f"Thank you for banking with us today. Goodbye {name.title()}!")
