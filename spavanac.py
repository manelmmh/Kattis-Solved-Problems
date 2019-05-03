from sys import stdin
h,m=map(int,stdin.readline().strip().split())
if h>23 and m>59:
    print("Error")
elif h==0:
    n=24
    result = ((n * 60) + m) - 45
    print(int(result / 60), result % 60)

else:
    result = ((h * 60) + m) - 45
    print(int(result / 60), result % 60)

