#!/usr/bin/python3


class User():
    """Creating a class User"""

    def __init__(self, name, email, password):  # CONSTRUCTOR METHOD
        """Declare and Initialize attributes of class User"""
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        """METHOD to change users password"""
        self.password = password
        print(f"Your password has been changed to: {self.password}")


user1 = User('ash', 'ash@nucamp.co', 'ashpassword')
print(user1.password)

user1.change_password('changepassword')


class BankUser(User):
    """Making a child class from parent class User"""

    def __init__(self, name, email, password):
        """Declare and Initialize attributes of CHILD class"""
        #  INITIALIZE attributes of PARENT CLASS
        super().__init__(name, email, password)
        self.balance = 0  # Belongs only to child class

    def check_balance(self):
        """METHOD to check bank account balance"""
        print(f"{self.name}, has a balance of {self.balance}")


bankuser1 = BankUser("Jane", "jane@nucamp.co", "bestpassword")
bankuser1.check_balance()
bankuser1.change_password("newpassword")
















