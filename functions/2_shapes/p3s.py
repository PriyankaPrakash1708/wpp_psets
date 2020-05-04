"""
Build a Diamond - SOLUTION

Create a function to print out a pyramid shape with some number of 
levels. By default, you should use star character (i.e. *), but it 
should accept other characters as well. Example:

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

def diamond(level, char='*'):

    x = list(range(1, level+1))

    for i in x:
        a = (level - i) * ' '
        b = i * char
        c = (i - 1) * char
        print(a + b + c)

    x.reverse()

    for i in x:
        if i == level:
            continue
        a = (level - i) * ' '
        b = i * char
        c = (i - 1) * char
        print(a + b + c)

diamond(5)
diamond(8, '$')
