"""
Control Flow I - SOLUTION

Print the numbers in some range until you find a multiple of 7. 
At that point, print "___ is the first multiple of 7 in this 
range." If the range does NOT include any multiples of 7, after 
you've printed the last number in the range, print "There are 
no multiples of 7 in this range.
"""

a = 24
b = 32

for i in range(a, b+1):
    if i % 7 != 0 and i == b:
        print(i)
        print(f'There are no multiples of 7 in the range {a}-{b}.')
    elif i % 7 != 0:
        print(i)
    elif i % 7 == 0:
        print(f'{i} is the first multiple of 7 in this range.')
        break


print('\n\n')


a = 15
b = 20

for i in range(a, b+1):
    if i % 7 != 0 and i == b:
        print(i)
        print(f'There are no multiples of 7 in the range {a}-{b}.')
    elif i % 7 != 0:
        print(i)
    elif i % 7 == 0:
        print(f'{i} is the first multiple of 7 in this range.')
        break