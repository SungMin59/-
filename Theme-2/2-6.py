import sys
A,B=map(int,sys.stdin.readline().split())
C=int(input())
if B+C<60:
	B+=C
else:
	B-=60-C
	if A==23:
		A=0
	else:
		A+=1
print(A,B)