from sys import stdin
n=int(stdin.readline().strip())
for i in range(n):
    x=int(stdin.readline().strip())

    if x%2==0:
        print("%d is even"%(x))
    else:
        print("%d is odd"%(x))