"""
Calculate Grade - SOLUTION

Write a program that will print the "letter" equivalent 
of the grade, for example:
when grade = 90 to 100 # -> expect A
when grade = 80 to 89 # -> expect B
when grade = 70 to 79 # -> expect C
when grade = 60 to 69 # -> expect D
when grade = 0 to 59 # -> expect F
when grade = -10 # -> expect Error
when grade = 10000 # -> expect Error
when grade = "lol skool sucks" # -> expect Error
"""

grade = 80
# grade = '15'
# grade = -8
# grade = 200

try:
    if grade > 100 or grade < 0:
        print("This grade isn't within the acceptable range.")
    elif grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 70:
        print('C')
    elif grade >= 55:
        print('D')
    else: 
        print('F')
except Exception as e:
    print(e) # this prints the actual error message
    print(e.__class__.__name__) # this prints what kind of error it is