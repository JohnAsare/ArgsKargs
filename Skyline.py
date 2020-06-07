# John Asare
# Jun 7 2020 12:57


""" Question: Define a function that takes in string and returns all letters that are even as uppercase
and odd letters as lowercase"""


def myfunc(statement):
    output = ' '
    for index, letter in enumerate(statement, 1):
        if index % 2 == 0:
            output += letter.upper()
        else:
            output += letter.lower()
    return output


def myfunc_one(text):
    processed = ''
    for i in range(len(text)):
        if i % 2 == 0:
            processed += text[i].lower()
        else:
            processed += text[i].upper()
    return processed


print(myfunc_one("Anthropomorphism"))
print(myfunc("Anthropomorphism"))
