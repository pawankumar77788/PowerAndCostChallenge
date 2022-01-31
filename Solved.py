# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
a = [4, 1, 5, 3]
x = 5
y = 2
l = list()
powerarr = list()
costarr = list()
for i in range(0, 3**len(a)):
    l.append(np.base_repr(i,base=3).zfill(len(a)))
for m in l:
    cost = 0
    power = sum(a)
    for n in range(0,len(m)):
        if(m[n] == '1'):
            cost = cost + x
            power = power - a[n]
        if(m[n] == '2'):
            cost = cost + y
            power = power - (a[n]*2)
    costarr.append(cost)
    powerarr.append(power)
print(list(filter(lambda x: x[0]<=0, list(zip(powerarr, costarr, l)))))
print(sorted(list(filter(lambda x: x[0]<=0, list(zip(powerarr, costarr, l)))),key = lambda y: y[1]))
