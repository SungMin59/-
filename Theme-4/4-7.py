import sys
N=int(input())
for i in range(N):
  arr=list(map(int,sys.stdin.readline().split()))
  a=sum(arr[1::])/arr[0]
  num = 0
  for k in arr[1::]:
    if k>a:
      num+=1
  print(f'{(num/len(arr[1::])*100):.3f}%')