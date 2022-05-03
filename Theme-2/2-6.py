import sys
A,B=map(int,sys.stdin.readline().split())
C=int(input())
if B+C<60:
	B+=C
else:
	A+=((B+C)//60)
	B=(B+C)%60
A-=24*(A//24)
print(A,B)