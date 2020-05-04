"""
Generate Traffic Light


Import python random package and use the randomint 
function to generate a random number between 1 & 3
"""

from random import randint

randn = randint(1, 3)

if randn == 1:
    print('red')
if randn == 2:
    print('green')
if randn == 3:
    print('yellow')

# if 1, print 'red'
# if 2, print 'green',
# if 3, print 'yellow'
