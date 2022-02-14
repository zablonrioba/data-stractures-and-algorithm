#  Using Euclid's Algorithm to find GCD between two intergers

"""
    step 1: for two intergers x and y , where  x > y , divide x by y.
    step 2: if the reminder r is 0  then stop : GCD is y 
    step 3: else set x to y, y to r and repeat step step on till r is o.
"""

def gcd(x,y):
    while ( y !=0):
        t = x
        x = y
        y = t % y

    return x

print(gcd(33,3))