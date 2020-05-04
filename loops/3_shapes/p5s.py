"""
Build a Diamond I - SOLUTION

Use a FOR loop to print a diamond of stars that looks like this:

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

level = 5

x = list(range(1, level+1))

for i in x:
    a = (level - i) * ' '
    b = i * '*'
    c = (i - 1) * '*'
    print(a + b + c)

x.reverse()

for i in x:
    if i == level:
        continue
    a = (level - i) * ' '
    b = i * '*'
    c = (i - 1) * '*'
