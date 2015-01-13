import math
# let f(x) = cos(e^(x^2) + x^3). ((f(1+0.1) - 2f(1) + f(1-0.1))/(0.1^2)) 
def f(x):
    return math.cos(math.pow(math.e, math.pow(x, 2))) + math.pow(x, 3)

for h in [0.1, 0.05, 0.025]:
    print(f(1 + h))
