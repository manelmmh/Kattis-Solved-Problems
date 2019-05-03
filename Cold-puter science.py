from sys import stdin
n=int(stdin.readline().strip())
t=[int(i)for i in stdin.readline().strip().split()]
count=0
for i in range(n):
    if t[i] < 0:
        count += 1


print(count)
