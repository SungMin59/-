import sys
N=int(input())
arr=list(map(int,sys.stdin.readline().split()))
MAX=max(arr)
arr=map(lambda x:x/MAX*100,arr)
print(sum(arr)/N)