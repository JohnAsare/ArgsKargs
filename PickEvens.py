# John Asare
# Jun 7 2020 12:32


""" Problem: Define a function that takes in many arguments but returns a list of those that just
even numbers"""


def myfunc(*args):
    return [number for number in args if number % 2 == 0]


print(myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
