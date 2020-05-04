"""
Generate Phone Number w/Area Code

Generate a random phone number using these SPECS:
- Should be a string in this format: 1-718-786-2825
- Must randomly choose one of these area codes: 646, 718, 212

Use ONLY basic data types and conditional statements/logic.
"""

from random import randint

areacode = randint(1, 3)

phone_number = "1-"
if areacode == 1:
    phone_number += "718"
if areacode == 2:
    phone_number += "646"
if areacode == 3:
    phone_number += "212"

phone_number += f"-{randint(100,999)}-{randint(1000,9999)}"
print(phone_number)

# OR

from random import choice, randint

areacode = choice([646, 718, 212])
exch_code = randint(100, 999)
linecode = randint(1000, 9999)

phone_number = f'1-{areacode}-{exch_code}-{linecode}'
print(phone_number)
