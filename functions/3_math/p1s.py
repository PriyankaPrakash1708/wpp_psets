"""
Sign of Product - SOLUTION

Given three numbers, without multiplying, write a function 
called "product_sign()" to determine the sign of their product. 

EXAMPLE1: -5, 6, -4 ==> returns 'positive'
EXAMPLE2: 5, -6, 4 ==> returns 'negative'
"""

def product_sign(a,b,c):
    """ 
    0 Trues/negs ==> pos sign | sum == 0
    1 Trues/negs ==> neg sign | sum == 1
    2 Trues/negs ==> pos sign | sum == 2
    3 Trues/negs ==> neg sign | sum == 3
    """
    sum = (a < 0) + (b < 0) + (c < 0)

    if sum == 1 or sum == 3:
        sign = 'negative'
    else:
        sign = 'positive'

    return sign

s1 = product_sign(2, -10, 6)
s2 = product_sign(-2, -10, 6)

print(s1)
print(s2)

