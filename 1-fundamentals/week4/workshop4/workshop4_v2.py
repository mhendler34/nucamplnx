#!/usr/bin/python3

class User:  # TASK 1
    """Creating a User class"""

    def __init__(self, name, pin, password):  # TASK 1
        """Constructor Method: Declare & Initialize attributes"""
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):  # TASK 2
        """Method: Changes name of the user"""
        self.name = new_name

    def change_pin(self, new_pin):  # TASK 2
        """Method: Changes pin of the user"""
        self.pin = new_pin

    def change_password(self, new_password):  # TASK 2
        """Method: Changes password of the user"""
        self.password = new_password


class BankUser(User):  # TASK 3
    """Creating a BankUser subclass of User class"""

    def __init__(self, name, pin, password):  # TASK 3
        """Constructor Method: Declare & Initialize attributes"""
        super().__init__(name, pin, password)
        """Inheriting attributes from parent class"""

        self.balance = 0  # BankUser attribute

    def show_balance(self):  # TASK 4
        """Method: Print user balance"""
        print(f"{self.name}'s account balance: {self.balance}.")

    def deposit(self, amount):  # TASK 4
        """Method: Adds deposits to balance"""
        self.balance += amount
        print(f"${self.balance}: deposited into {self.name}'s account.")

    def withdraw(self, amount):  # TASK 4
        """Method: Subtracts money from balance"""
        if self.balance > 0:
            self.balance -= amount
        else:
            print("Sorry, insufficient funds to withdraw")

    def transfer_money(self, amount, account):  # TASK 5
        """Method: Transfers money if conditions are met"""
        print(f"{self.name}: transferring ${amount} to {account.name}")
        print("Authentication required\n")
        response = input(f"Enter {self.name}'s PIN: \n")
        if response == self.pin:
            print("Transfer authorized")
            print(f"Transferring ${amount} to {account.name}\n")
            self.balance -= amount
            account.balance += amount
            return True
        else:
            print("INVALID PIN")
            return False

    def request_money(self, amount, account):
        """METHOD: Request money"""
        print(f"{self.name}: requests ${amount} from {account.name}\n")
        print("Authentication required\n")
        response = input(f"Enter {account.name}'s PIN: ")
        if response == account.pin:
            user_password = input(f"Please enter {self.name}'s password: ")
            if user_password == self.password:
                self.balance += amount
                account.balance -= amount
                print("Request authorized")
                return True
            else:
                print("INVALID password")
                return False
        else:
            print("INVALID PIN")
            return False


""" Driver Code for Task 5 - deposit money """
user5 = BankUser('MERLIN', '1234', 'qwerty12345')
user6 = BankUser('KING ARTHUR', '1234', 'qwerty12345')
user6.deposit(400)
user6.show_balance()
user5.show_balance()
user5.request_money(400, user6)
user6.show_balance()
user5.show_balance()

""" Driver Code for Task 5 - transfer money """
# user5 = BankUser('MERLIN', '1234', 'qwerty12345')
# user6 = BankUser('KING ARTHUR ', '1234', 'qwerty12345')
# user6.deposit(5000)
# user6.show_balance()
# user5.show_balance()
# user6.transfer_money(500, user5)
# user6.show_balance()
# user5.show_balance()
# user5.transfer_money(500, user6)
# user5.show_balance()
# user6.show_balance()

""" Driver Code for Task 4 """
# user4 = BankUser('zash', '1234', 'qwerty12345')
# user4.show_balance()
# user4.deposit(200)
# user4.show_balance()
# user4.withdraw(100)
# user4.show_balance()
# user4.withdraw(200)
# user4.show_balance()
# user4.deposit(300)
# user4.show_balance()

""" Driver Code for Task 3 """
# user3 = BankUser('dash', '1234', 'qwerty12345')
# print(user3.name, user3.pin, user3.password, user3.balance)

""" Driver Code for Task 2 """
# user2 = User('bash', '1234', 'qwerty12345')
# print(f"USER1: {user2.name} {user2.pin} {user2.password}")
# user2.change_name('cash')
# user2.change_pin('2345')
# user2.change_password('asdf1234')
# print(f"USER2: {user2.name} {user2.pin} {user2.password}")

""" Driver Code for Task 1 """
# user1 = User('bash', '1234', 'qwerty12345')
# print(f"Name: {user1.name}")
# print(f"PIN: {user1.pin}")
# print(f"Pword: {user1.password}")
