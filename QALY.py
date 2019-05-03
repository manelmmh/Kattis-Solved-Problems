from sys import stdin
N=int(stdin.readline().strip())
total=0
for i in range(N):
    q,y=[float(x) for x in stdin.readline().strip().split()]
    QALY=q*y
    total+=QALY
print(format(total,'.3f'))