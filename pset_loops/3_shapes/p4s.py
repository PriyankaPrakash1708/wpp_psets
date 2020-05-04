"""
Build a Pyramid II - SOLUTION

Use a WHILE loop to print a pyramid of stars that looks like this:

    *
   ***
  *****
 *******
*********

"""

stars = 1
rows = 5
chars = (rows - 1) + rows

while stars <= chars:
    if stars % 2 != 0:
        spaces = int((chars - stars) / 2)
        print(' '*spaces+'*' * stars+' '*spaces)
    stars += 1
