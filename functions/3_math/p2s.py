"""
Simple Interest Calculator - SOLUTION

Write a function called "simple_interest" that intakes an initial 
lump sum of money, a monthly interest rate, and some number of 
months. Based on this, the function should calculate how much 
**interest** will be earned after the given numbers months as well
as how much money there will be in **total**. 
"""

def simple_interest(p,r,t):
    """Simple interest formula is A = P(1 + rt), where...
    P = principal amount of money
    r = interest rate
    t = number of time periods the principal will earn interest"""
    
    try:
        p, r, t = float(p), float(r), float(t)
        i = (p*r*t)/100
        A = p + i
        A = round(A, 2)
        return i, A
    except Exception as e:
        return e

p = 1500
r = 2.4
t = 60

interest_accrued, total = simple_interest(p,r,t)

print(f'\nPrincipal: ${p} \nInterest Earned: ${interest_accrued} \nTotal Funds: ${total}')