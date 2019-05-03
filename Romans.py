from sys import stdin
X=float(stdin.readline())

N=1000*(5280/4854)*X
print(int(round(N,0)))