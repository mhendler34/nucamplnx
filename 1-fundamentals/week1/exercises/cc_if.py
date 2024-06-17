#!/usr/bin/python3
"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""
grade_to_test = 0

if grade_to_test == 100:
    print("A+")
elif grade_to_test >= 90:
    print("A")
elif grade_to_test >= 80:
    print("B")
elif grade_to_test >= 70:
    print("C")
elif grade_to_test >= 50:
    print("D")
else:
    print("F")
