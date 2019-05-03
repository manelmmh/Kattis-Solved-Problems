from sys import stdin
import numpy as np
total=[]
for i in range(1,6):
    grade=[int(x) for x in stdin.readline().strip().split()]
    total.append(sum(grade))
totalnp=np.array(total)
index_max=np.argmax(totalnp)

print((index_max + 1), max(total))
