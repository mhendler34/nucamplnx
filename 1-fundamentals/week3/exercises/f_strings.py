#!/usr/bin/python3

number = 5
square = f"The square of {number} is {number ** 2}."
print(square)

my_string = "Hello World"
formatted_string = f"{my_string.upper()} has {len(my_string)} characters."
print(formatted_string)

pi = 3.14159
formatted_pi = f"Pi to three decimal places is {pi:.3f}."
print(formatted_pi)

name = 'Alice'
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."

multiline_fstring = f"""
Name: {name}
Age: {age}
Greeting: {greeting}
"""
print(multiline_fstring)
