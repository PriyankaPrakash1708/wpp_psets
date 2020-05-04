"""
Ordering Random Numbers - SOLUTION

Create a list called numbers, containing 6 randomly generated numbers and sort it in descending order.

Bonus Challenge: See if you can randomly generate this list in 
one line of code.

Bonus Bonus: See if you can create the list in one line in two
different ways.
"""

from random import randint, sample

numbers = sample(range(0, 100), 6)
numbers.sort(reverse = True)
print(numbers)

# OR 

numbers = []
numbers.append(randint(0, 100))
numbers.append(randint(0, 100))
numbers.append(randint(0, 100))
numbers.append(randint(0, 100))
numbers.append(randint(0, 100))
numbers.append(randint(0, 100))
numbers.append(randint(0, 100))

print(f'Unsorted: {numbers}\n')


numbers.sort(reverse = True)
# OR... numbers = sorted(numbers, reverse = True)

print(f'Sorted: {numbers}\n')

"""
ALTERNATIVES
from random import randint, sample

# random.sample()
numbers = sample(range(0, 100), 6)
numbers.sort(reverse = True)
print(numbers)

# while loop
numbers = []
while len(numbers) < 6:
    numbers.append(randint(0, 100))

numbers.sort(reverse = True)
print(numbers)

# list comprehension
numbers = [randint(0, 100) for num in numbers]
numbers.sort(reverse = True)
print(numbers)
"""