import sys
N=int(input())
inp = [x for x in map(int,sys.stdin.readline().rstrip().split())]
max = 0
for i in range(inp):
	if inp[i]>inp[i+1]:
		