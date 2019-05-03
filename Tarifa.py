from sys import stdin
X= int(stdin.readline().strip())
N= int(stdin.readline().strip())
m=0
for i in range(N):
    P= int(stdin.readline().strip())
    m=(m+X)-P
print(m+X)


