from sys import stdin
A, I = [int(x) for x in stdin.readline().strip().split()]

print(A*I-(A-1))
