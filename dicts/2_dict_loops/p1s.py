"""
Contacts - SOLUTION

You went to a conference and got people to sign up for text 
updates from your startup. Go through this dict to make the 
phone numbers readable to a computer. 

Hint: It can't include any non-numeric characters.
"""

contacts = {
    'Jamie': '1.192.168.0143',
    'Kartik': '1-837-209-1121',
    'Grant': '1.826.386.1758',
    'Claude': '19352979447',
    'Monique': '1 702 716 5353',
    'Sohom': '1-576-619-6100'
}

for name, num in contacts.items():
    new_num = ''
    for char in num:
        if char in '0123456789':
            new_num += char
    contacts.update({name: new_num})

print(contacts)

# OR

contacts = {
    'Jamie': '1.192.168.0143',
    'Kartik': '1-837-209-1121',
    'Grant': '1.826.386.1758',
    'Claude': '19352979447',
    'Monique': '1 702 716 5353',
    'Sohom': '1-576-619-6100'
}

for name, num in contacts.items():
    for char in num:
        if char not in '0123456789':
            num = num.replace(char, '')
    contacts.update({name: num})

print(contacts)