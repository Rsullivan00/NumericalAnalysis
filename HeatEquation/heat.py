import numpy as np
import math
import matplotlib.pyplot as plt

def heat_2d():
    dx=0.05
    dt=.5*dx*dx
    x = []
    for x_i in range(-20, 21):
        x.append(dx*x_i)
        
    t = []
    for t_i in range(0, 401):
        t.append(t_i*dt)

    f=np.zeros(shape=(len(x),len(t)))
    for j in range(len(f)):
        f[j,0] = math.exp(-5*abs(x[j]))


    for i in range(len(f)):
        f[0,i] = 0
        f[-1,i] = 0

    for i in range(len(t)-1):
        for j in range(1,len(f)-1):
            f[j,i+1] = f[j,i] + dt*((f[j+1,i] - 2*f[j,i] + f[j-1,i])/(dx*dx))

    # Draw contour
    plt.figure('2D heat equation')
    plt.contourf(t,x,f,100)
    plt.xlabel('t')
    plt.ylabel('x')
    plt.savefig('heat2d.png')
    plt.show()

def heat_3d():
    dx=0.05
    dy=0.05
    dt=.5*dx*dx
    x = []
    for x_i in range(-20, 21):
        x.append(dx*x_i)
    y = []
    for y_i in range(-20, 21):
        y.append(dy*y_i)
        
    t = []
    for t_i in range(0, 401):
        t.append(t_i*dt)

    f=np.zeros(shape=(len(x),len(y),len(t)))
    for i in range(len(f)):
        for j in range(len(f[i])):
            f[i,j,0] = math.exp(-5*abs(x[i])) * math.exp(-5*abs(y[j])) 

    for i in range(len(f)):
        for j in range(len(t)):
            f[i,0,j] = 0
            f[i,-1,j] = 0
            f[0,i,j] = 0
            f[-1,i,j] = 0

    for i in range(len(t)-1):
        for j in range(1,len(f)-1):
            for k in range(1,len(f[j])-1):
                f[j,k,i+1] = f[j,k,i] + dt*((f[j+1,k,i] - 2*f[j,k,i] + f[j-1,k,i])/(dx*dx)) + dt*((f[j,k+1,i] - 2*f[j,k,i] + f[j,k-1,i])/(dy*dy)) 

    # Draw contour
    #plt.figure()
    #plt.contourf(t,x,y,f,100)
    #plt.show()

heat_2d()
heat_3d()
