import sys
A,B=map(int,sys.stdin.readline().split())
C=int(input())
if B+C<60:
	B+=C
else:
	B-=60-C
	A+=C//60
	A=A-A//1440
print(A,B)