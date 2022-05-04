import sys
N,X = map(int,sys.stdin.readline().rstrip().split())
inp = [x for x in map(int,sys.stdin.readline().rstrip().split())]
for i in inp:
	if X>i:
		