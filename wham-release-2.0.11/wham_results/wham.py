import matplotlib.pyplot as plt
import numpy as np
f = open('freefile_kcal.txt')
j = f.read()
j = j.split('\n')
j = j[2:]
j = j[:39]

for i in range(len(j)):
    k=j[i].split('\t')[:2]
    for l in range(len(k)):
        k[l] = float(k[l])
    j[i] = k

j = np.array(j)

plt.plot(j[:,0],j[:,1],'--o')
plt.xlabel('N')
plt.ylabel('-log P(N)')
plt.savefig('prob_dist.png')

