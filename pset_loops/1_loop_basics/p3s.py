"""
Temperature Conversions - SOLUTION

You're studying climate change, and over the last 3 years, 
you've recorded the temperature at noon every day in degrees 
Fahrenheit (F). The var sampleF holds a portion of those 
recordings. Convert each item in this list into degrees 
Celsius and add the results to a list called sampleC.

The conversion formula is: 
Celsius = (Fahrenheit - 32) * 5.0/9.0
"""

sampleF = [91.4, 82.4, 71.6, 107.6, 115.6]

sample_temps = {}

for f in sampleF:
    c = (f - 32)*(5/9)
    sampleC.append(c)