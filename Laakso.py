#%%

import numpy as np
import matplotlib.pyplot as plt

#%%

def Laaksofrac(endpoints,a,angle,depth,colour):
    b = (1-a)/(2*np.cos(angle))
    # b = 1/2
    k = complex(0,angle)
    
    if depth >= 1 and type(depth) == int:
        endpoints1 = a*endpoints
        Laaksofrac(endpoints1,a,angle,depth-1,"k-")
        
        endpoints2 = a + b*np.exp(k)*endpoints
        Laaksofrac(endpoints2,a,angle,depth-1,"b-")
        
        endpoints3 = a + b*np.exp(-k)*endpoints
        Laaksofrac(endpoints3,a,angle,depth-1,"r-")
        
        endpoints4 = 1 - b*np.exp(-k)*endpoints
        Laaksofrac(endpoints4,a,angle,depth-1,"y-")
        
        endpoints5 = 1 - b*np.exp(k)*endpoints
        Laaksofrac(endpoints5,a,angle,depth-1,"g-")

    elif depth == 0:
        plt.plot(np.real(endpoints),np.imag(endpoints),colour,linewidth = 1.0)
        plt.plot(np.real(endpoints),np.imag(endpoints),"k.",linewidth = 2.0)
        
    else:
        print("Invalid depth")

#%%

pi = np.pi
endpoints = np.array([0,1])
a = 0.5
angle = pi/6
depth = 5

plt.figure(figsize = (8,5))
Laaksofrac(endpoints,a,angle,depth,"r-")
plt.gca().set_aspect(1.0)
# %%
