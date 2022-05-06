import sys
N=int(input())
for i in range(N):
  a,l=sys.stdin.readline().split()
  print( *list(map(lambda x:str(x)*int(a),l)),sep='')