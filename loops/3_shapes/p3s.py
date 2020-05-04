"""
Build a Pyramid I - SOLUTION

Use a FOR loop to print a pyramid of stars that looks like this:

    *
   ***
  *****
 *******
*********

"""

level = 5

for i in range(1, level+1):
    a = (level-i) * ' '
    b = i * '*'
    c = (i - 1) * '*'
    print(a + b + c)