"""
GCD - SOLUTION

Find the greatest common denominator (GCD) of two number input by a user. Then print out 'The GCD of <first number> and <second number> is <your result>.'
"""

print('Enter two numbers to find their greatest common denominator.')

user_input1 = input('First number: ')
user_input2 = input('Second number: ')

a = int(user_input1)
b = int(user_input2)

print(f'The GCD of {a} and {b} is: ')

while b != 0:
    a, b = b, a % b

print(a)

"""
a = 64
b = 24


a = 24
b = 16

a = 16
b = 8

a = 8
b = 0
"""

"""
a = 24
b = 64


a = 64
b = 24 (24 % 64 is 0 remainder 24)

a = 24
b = 16

a = 16
b = 8

a = 8
b = 0
"""

# OR 

num1 = int(input('First number: '))
num2 = int(input('Second number: '))

a = []
b = []

for factor in range(1, num1):
    if num1 % factor == 0:
        a.append(factor)
print(a)

for factor in range(1, num2):
  if num2 % factor == 0:
    b.append(factor)
print(b)

gcd = max(set(a) & set(b))

print(f"The GCD of {num1} and {num2} is {gcd}.")


# OR 

num1 = int(input('First number: '))
num2 = int(input('Second number: '))

denominators = []

upper_bound = min((num1 + 1), (num2 + 1))

x = range(1, upper_bound)

for i in x : 
    if num1 % i == 0 and num2 % i == 0:
        denominators.append(number)

gcd = max(denominators)

print(f"The GCD of {num1} and {num2} is {gcd}.")