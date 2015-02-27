import numpy 

a = [[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]]
u,s,v = numpy.linalg.svd(a)
print(u)
print(s)
print(v)
