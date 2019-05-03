from sys import stdin
default=[1,1,2,2,2,8] # create a list of the standard combination
found=stdin.readline().strip().split() # read a combination from user
result=[int(x)-int(y) for x,y in zip(default,found)] # subtract the elements of each pair resulted from zip
print(" ".join([str(x) for x in result]))
