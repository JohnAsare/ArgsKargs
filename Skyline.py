# John Asare
# Jun 7 2020 12:57


""" Question: Define a function that takes in string and returns all letters that are even as uppercase
and odd letters as lowercase"""


def myfunc(statement):
    for index, letter in enumerate(statement):
        if index % 2 == 0:
            print(letter.upper())
        else:
            print(letter.lower())


print(myfunc("Thisisaboy"))
