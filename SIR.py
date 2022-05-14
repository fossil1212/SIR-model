from matplotlib import pyplot as plt


S = []
I = []
R = []
DT = []
beta = 0.5
gamma = 0.3
s = 99
i = 1
r = 0
N = 100
dt = 0.001
m = 0
Input = None
d = 10000

while s>0 and i>0 and r>=0:
    S.append(s)
    I.append(i)
    R.append(r)
    DT.append(m)
    ds = (-beta/N*i*s)*dt
    di = (beta/N*i*s - i*gamma)*dt
    dr = (i*gamma)*dt
    s += ds
    i += di   
    r += dr
    m += dt
    
    if m >= 100:
        break


            


plt.plot(DT, S)
plt.plot(DT, I)
plt.plot(DT, R)
plt.show()