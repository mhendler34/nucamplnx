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
