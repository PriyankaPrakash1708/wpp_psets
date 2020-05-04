"""
Predators & Prey
"""

# A) Create a dict called "pred_prey", containing:
### 3 carnivorous marine animals
### For each carnivore, 3 examples of its prey

pred_prey = {
    'dolphin': ['shrimp', 'herring', 'squid'],
    'orca whale': ['sea turtle', 'harp seal', 'squid'],
    'great white shark': ['sea lion', 'sea turtle', 'harp seal']
}

# B) Print out the 2nd predator and its prey in this format:
#### predator2: prey1, prey2, & prey3

p = list(pred_prey.items())
pred2, prey2 = p[1][0], p[1][1]
print(f'{pred2}: {prey2[0]}, {prey2[1]}, {prey2[2]}')


# C) Print a unique collection of all the prey in a variable called "prey".

prey_lists = list(pred_prey.values())
prey = prey_lists[0] + prey_lists[1] + prey_lists[2]
prey = set(prey)
print(prey)

"""
OR 

prey_lists = list(pred_prey.values())
prey = []
prey.extend(prey_lists[0])
prey.extend(prey_lists[1])
prey.extend(prey_lists[2])
prey = set(prey)
print(prey)

OR

pred_prey = {
    'octopus': ['clam', 'crab', 'crayfish'], 
    'seals': ['sea birds', 'herring', 'salmon'], 
    'shark': ['squid', 'dolphin', 'tuna']
}

prey = []

for i in list(pred_prey.values()):
    prey.extend(i)

prey = set(prey)
print(prey)
"""
