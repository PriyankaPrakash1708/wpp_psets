"""
Lists to Dicts - SOLUTION

Turn these two lists into a dict called grades.
"""

names = ['Taq', 'Zola', 'Valerie', 'Veronica']
scores = [[98, 89, 92, 94], [86, 45, 98, 100], 
[100, 100, 100, 100], [76, 79, 80, 82]]

unique_names = set(names)

if names == unique_names and len(names) == len(scores):
    grades = dict(zip(names, scores))
 
"""
{'Taq': [98, 89, 92, 94], 'Zola': [86, 45, 98, 100], 
'Valerie': [100, 100, 100, 100], 'Veronica': [76, 79, 80, 82]}
"""

 