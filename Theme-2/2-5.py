import sys
A,B=map(int,sys.stdin.readline().split())
if B-45>=0:
	B -= 45
	A-=1
else:
	B += 15
	if A==0:
		A=23
	else:
		A-=1
print(A,B)