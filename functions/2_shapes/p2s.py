"""
Build a Pyramid - SOLUTION

Create a function to print out a pyramid shape with some number of 
levels. By default, you should use star character (i.e. *), but it 
should accept other characters as well. Example:

    *
   ***
  *****
 *******
*********

"""

def pyramid(level, char='*'):
    for i in range(1, level+1):
        a = (level-i) * ' '
        b = i * char
        c = (i - 1) * char
        print(a + b + c)


pyramid(5)
pyramid(8, '^')