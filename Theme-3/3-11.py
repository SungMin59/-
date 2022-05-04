import sys
N,X = map(int,sys.stdin.readline().split())
inp = [x for x in map(int,sys.stdin.readline().split())]
arr = []
for i in inp:
	if X<i:
		arr.append(i)
print(i)