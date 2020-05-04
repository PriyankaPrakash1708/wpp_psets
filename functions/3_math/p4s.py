"""
Sum Multiples - SOLUTION

Write a function called "sum_multiples" that takes two numbers 
and returns the sum of their multiples, while the sum is 
between 0 and some limit/upper bound. These items should be 
generalized as parameters. If any inputs aren't integers, print 
a string with some error message.
"""


def sum_multiples(num1,num2,limit):
    """take two numbers and find the sum of their multiples 
    until sum reaches some upper limit."""

    if type(num1) != int or type(num2) != int or type(limit) != int:
        return f'All inputs must be integers'

    sum = 0

    if num1 > limit or num2 > limit:
        return sum
    elif num1 + num2 > limit:
        return sum

    i = 1

    while sum < limit:
        x = (num1 * i) + (num2 * i)
        if sum + x > limit:
            return sum
        else:
            sum += x
            i += 1

    return sum

# num1 > limit
total1 = sum_multiples(12,8,10)
print(total1)

# num2 > limit
total2 = sum_multiples(3,17,12)
print(total2)

# num1 + num2 > limit
total3 = sum_multiples(21,9,29)
print(total3)

# num1 + num2 == limit
total4 = sum_multiples(8,5,13)
print(total4)

# limit > num1 + num2
total5 = sum_multiples(4,8,42)
print(total5)

# at least one input is not an int
total6 = sum_factors(3,'8',18)
print(total6)
