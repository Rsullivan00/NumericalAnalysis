# Rick Sullivan
# 6 January 2015
# 
# Requires python 3
import math

def a(x):
    return (20*x + 21/math.pow(x, 2))/21

def b(x):
    return x - (math.pow(x, 3) - 21)/(3*math.pow(x, 2))

def c(x):
    return x - (math.pow(x, 4) - 21*x)/(math.pow(x, 2) - 21)

def d(x):
    return math.pow(21/x, 0.5)

# Provides a fixed point iteration on the function f starting at the point p
def fixedpoint(p, f, iterations=10):
    for i in range(iterations):
        p = f(p)
        print("Iteration " + str(i+1) + ": p=" + str(p))

    return p

# Function used in question 3
def g(x):
    return math.pow((x + 3)/(math.pow(x, 2) + 2), 0.5)

functions = [a, b, c, d]
for f in functions:
    print("Function " + f.__name__ + ":")
    fixedpoint(1, f)
    print("")
