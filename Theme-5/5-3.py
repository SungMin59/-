N=int(input())
# 등차수열 합의 대칭성 이용(등차중항)
sum=0
if len(str(N))<3:
  sum=N
else:
  sum=99
  for i in range(100,N+1):
    a=list(map(int,str(i)))
    if a[0]+a[-1]==a[1]+a[-2]:
      sum+=1
print(sum)