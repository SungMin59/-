import sys
#백트래킹
A,B,C=map(int,sys.stdin.readline().split()))
if A==B==C:
	print(10000+A*1000)
if A==B or B==C:
	print(B)
if A==C:
	print(*max(d))