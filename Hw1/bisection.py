# Rick Sullivan
# 6 January 2015
# 
# Requires python 3
import math

# Function used in question 1) of homework
# Used this to verify my answer
def f(x):
    return math.sqrt(x) - math.cos(x)

# Function used in question 2) of homework
def g(x):
    return 3*x - math.pow(math.e, x)

# Uses the bisection method to approximate the root of
# the function f over the interval a <= x <= b
# Precision can be set in two ways:
#   1) Set the number of iterations the algorithm will take
#   2) Give a number of decimal places, which will calculate
#       how many iterations are needed
def bisection(a, b, f, iterations=None, decimal_places=None):
    if iterations is None and decimal_places is None:
        raise Exception("Must provide either number of iterations or decimal places")
    if decimal_places is not None:
        iterations = math.ceil(math.log10(abs(b-a) * math.pow(10, decimal_places)) / math.log10(2))
    p = (b+a)/2
    for i in range(iterations):
        if f(p)*f(a) < 0:
            b = p
        else:
            a = p

        p = (b+a)/2
        print("Iteration " + str(i+1) + ": p=" + str(p))

    return p

# Verify question 1
# bisection(0, 1, f, iterations=3)
# Generate accurate answer for question 2
bisection(1, 2, g, decimal_places=5)
