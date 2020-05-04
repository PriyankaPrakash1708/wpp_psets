"""
GPA Calculator - SOLUTION

Write a function called "simple_gpa" to find GPA when 
student enters a letter grade as a string. Assign the 
result to a variable called "gpa".

Use these conversions:
A+ --> 4.0
A --> 4.0
A- --> 3.7
B+ --> 3.3
B --> 3.0
B- --> 2.7
C+ --> 2.3
C --> 2.0
C- --> 1.7
D+ --> 1.3
D --> 1.0
D- --> 0.7
F --> 0.0
"""

def simple_gpa(grade):
    """This takes a letter grade and returns the corresponding GPA using the simplest GPA formula."""

    grade_gpa_conversions = {
        'A+': 4.0,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'D-': 0.7,
        'F': 0.0
    }

    try:
        gpa = grade_gpa_conversions[grade]
        return gpa
    except Exception as e:
        return f'{e.__class__.__name__}: {e}'


gpa1 = simple_gpa('B+')
print(gpa1)

gpa2 = simple_gpa('Q')
print(gpa2)