"""
Build a Triangle - SOLUTION

Create a function to print out a triangle with some number of levels. 
By default, you should use star character (i.e. *), but it should
accept other characters as well. Example:

*
**
***
****
*****

"""

def triangle(levels, char='*'):
	for i in range(1,levels+1):
        print(char * i)


triangle(5)
triange(8, '&')