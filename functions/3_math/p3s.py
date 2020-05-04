"""
Sum Factors - SOLUTION

Write a function called "sum_factors" that takes two numbers 
and returns the sum of their factors, while the sum is
between 0 and some limit/upper bound. These items should be 
generalized as parameters. Do NOT double-count numbers that 
are factors of BOTH the original two numbers entered.  If any 
inputs aren't integers, print a string with some error message.
"""

def sum_factors(num1,num2,limit):
    """take two numbers and find the sum of their factors until 
    sum reaches some upper limit. this does NOT double-count 
    common factors of the original two numbers entered"""

    if type(num1) != int or type(num2) != int or type(limit) != int:
        return f'All inputs must be integers'

    higher = max([num1, num2])
    sum = 0

    for i in range(1, (higher + 1)):
        if num1 % i == 0 or num2 % i  == 0:
            x = sum + i
            if x > limit:
                return sum
            else:
                sum += i

    return sum

# sum of ALL factors never reaches limit
total1 = sum_factors(3,8,21) # 1 + 2 + 3 + 4 + 8 = 18
print(total1)

# sum of ALL factors == limit
total2 = sum_factors(3,8,18) # 1 + 2 + 3 + 4 + 8 = 18
print(total2)

# can sum several factors before reaching limit
total3 = sum_factors(3,8,18)
print(total3)

# at least one input is not an int
total4 = sum_factors(3,'8',18)
print(total4)