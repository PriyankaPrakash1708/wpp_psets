"""
Generate Phone Number w/Area Code

For each person in the dictionary below, insert a 
randomly generated phone number. Make sure to use 
these SPECS:
- Should be a string in this format: 1-718-786-2825
- Must randomly choose one of these area codes: 646, 718, 212

Hint: Another function from the random module might be useful
"""

from random import choice, randint

people = {
    'Melody': '1-',
    'Sergei': '1-',
    'Brandon': '1-',
    'Leo': '1-',
    'Priscilla': '1-'
}

for name, num in people.items():
    num += choice(['646', '718', '212'])
    num += f"-{randint(100,999)}-{randint(1000,9999)}"
    #people[name] = (num)
    people.update({name:num})
    print(f'{name}: {num}')


