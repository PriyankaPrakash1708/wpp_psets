"""
Factorial - SOLUTION

Find the factorial of a number input by a user. 
Then print out the factors within the factorial and 
then print out the actual numeric answer. Hint: The 
formula for the factorial a number n is below:

n! = n*(n-1)!


Example output:
8! = 8*7*6*5*4*3*2*1
8! = 40320
"""

initial = int(input('Enter a number to find its factorial: '))

n = initial
factors = [n]
factorial = n

while n > 1:
    n -= 1
    factors.append(n)
    factorial *= n

print(f'{initial}! = {factorial}')
print(f'Factors: {'*'.join(factors)}')

# OR

n = int(input('Enter a number to find its factorial: '))

n = 8

factorial = 1
factors = []

for x in range(1, n+1):
    factorial *= x
    factors.append(x)

factors.reverse()

print(f'{n}! = {factorial}')
print(f'Factors: {'*'.join(factors)}')