import sys
import math as m
N=int(input())
a=list(map(int,sys.stdin.readline().split()))
p=0
for i in a:
  c=0
  if i>1:
    for k in range(2,m.isqrt(i)+1):
      if i % k == 0:
        c+=1
    if c==0:
      p+=1
print(p)

# 답
# sosu = 0
# for num in a:
#     error = 0
#     if num > 1 :
#         for i in range(2, num):
#             if num % i == 0:
#                 error += 1
#         if error == 0:
#             sosu += 1
# print(sosu)