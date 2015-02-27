import numpy as np 
a = [[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]]
u,s,v = np.linalg.svd(a)
print('U:%s' % u)
print('S:%s' % s)
print('V:%s' % v)

# Approximations
u_2 = [[x] for x in u[:,0]]
s_2 = s[0]
v_2 = v[0]
print('Approximation reconstruction:\n%s' % (np.multiply(np.multiply(u_2, s_2), v_2)))
