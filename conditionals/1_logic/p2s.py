"""
Sign of Product - SOLUTION

Given three numbers, a, b, c, without multiplying, determine the sign of their product.

EXAMPLE1: a = -5, b = 6, c = -4, print 'positive'
EXAMPLE2: a = 5, b = 6, c = -4, print 'negative'
"""

a = 2
b = -10
c = 6

if a < 0 and b < 0 and c < 0:
    print(True)
elif a < 0 and b < 0 and c > 0:
    print(False)
elif a < 0 and b > 0 and c < 0:
    print(False)
elif a < 0 and b > 0 and c > 0:
    print(True)

# OR

sum = (a < 0) + (b < 0) + (c < 0)

""" 
where True implies a negative...

0 Trues ==> pos sign | sum == 0
1 Trues ==> neg sign | sum == 1
2 Trues ==> pos sign | sum == 2
3 Trues ==> neg sign | sum == 3
"""

if sum == 1 or sum == 3:
    print('Negative')
else:
    print('Positive')
