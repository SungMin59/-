import sys
A, B ,C= map(int, sys.stdin.readline().split())
print((A+B)%C)
print(((A%C)+(A%C))%C)
print((A*B)%C)
print(((A%C)*(A%C))%C)