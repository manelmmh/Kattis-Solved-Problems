from sys import stdin
string=stdin.readline().strip().split("-")
print("".join([x[0]for x in string]))

