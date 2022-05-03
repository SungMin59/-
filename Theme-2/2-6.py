import sys
A,B=map(int,sys.stdin.readline().split())
C=int(input())
if B+C<60:
	B+=C
print(A,B)