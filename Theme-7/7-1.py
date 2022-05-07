import sys
A,B,C=map(int,sys.stdin.readline().split())
x=-1 if C-B==0 else A//(C-B)+1
print(x if x > 0 else -1)
# a,b,c=map(int,input().split());print(a//(c-b)+1if c>b else-1)