"""
Any Uppercase - SOLUTION


Given a string, determine if there are any uppercase values in it.
Use only conditional statements and string methods
(you may have to look some up!)

EXAMPLE: str1 = "teSt", print True
"""


str1 = 'teSt'

if str1.islower() == True:
    print(True)
else:
    print(False)

# OR

if str1 == str1.lower():
    print(True)
else:
    print(False)
