#!/usr/bin/python3

from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print(f"User: {name.title()}")
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# Registration Intake
print("          === Automated Teller Machine ===          ")
print("REGISTRATION")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(f"{name.title()} has been registered, starting balance of ${balance}")

while True:
    print()
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    validate_name = input("Login name: ")
    validate_pin = input("Login PIN: ")
    if validate_name == name and validate_pin == pin:
        print("Successful Login!")
        break
    else:
        print("Invalid Credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option [1, 2, 3, 4]: ")
    if option == '1':
        # Calling show_balance() from account.py module
        account.show_balance(balance)
    elif option == '2':
        # Calling deposit() and reassigning return value to balance
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == '3':
        # Calling withdraw() and reassigning return value to balance
        balance = account.withdraw(balance)
        account.show_balance(balance)
    else:
        account.logout(name)
        break

