"""
Factors - SOLUTION

Find all factors of a number that a user inputs and print out 'The factors of <the_user_input_number> are: '.
"""

user_input = input("Enter a number to find its factors: ")
a = int(user_input)

print(f'The factors of {a} are: ')

for i in range(1, a + 1):
  if a % i == 0:
    print(i)