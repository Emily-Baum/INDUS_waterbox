import matplotlib.pyplot as plt
import statistics as s
    
T=300

# select number of water molecules in volume from plumed.out
f = open('plumed.out')
f = f.read()
f = f.split()
f = f[7::4]
f = f[100:]
f = [float(i) for i in f]

# calculate mean and variance of waters in box
nv0 = s.mean(f)
nv20 = s.variance(f)

# calculate parameters needed for simulation
dNstar = (nv20**.5)*4/(3**.5) # eq 8
k = 2*1.380649*6.022*T/(nv20*1000) # eq 4 and 7, with unit conversion factors

# print parameter values, use these in indus.input
print("dN* = {:.3f}".format(dNstar))
print("k = {:.3f} kj/mol".format(k))

