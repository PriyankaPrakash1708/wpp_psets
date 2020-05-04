"""
Build a Diamond II - SOLUTION
"""

# Use a WHILE loop to print a diamond of stars, like this:

"""
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

stars = 1
rows = 5
chars = (rows - 1) + rows

while stars <= chars:
    if stars % 2 != 0:
        spaces = int((chars - stars) / 2)
        print(' '*spaces+'*' * stars+' '*spaces)
    stars += 1

while stars >= 1:
  if stars % 2 != 0:
    spaces = int((chars - stars) / 2)
    print(' '*spaces+'*' * stars+' '*spaces)
  stars -= 1


for x in range(1,6):
    print((' ' * (5 - x)) + ('*' * ((x * 2) - 1))) 
