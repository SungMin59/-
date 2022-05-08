# 최소 단위 3*3
def pr(mx):
  if mx==1:
    return "*"
  M=pr(int(mx/3))
  arr=[]
  for k in M:
    arr.append(k*3) # M의 원소 증폭 1
  for k in M:
    arr.append(k+' '*int(mx/3)+k)
  for k in M:
    arr.append(k*3)  
  return arr
print(*pr(int(input())),sep='\n')





# 답
#   if mx ==1:
#     return "*"

#   temp=pr(int(mx/3))
#   arr=[]

#   for S in temp:
#     arr.append(S*3)
#   for S in temp:
#     arr.append(S+' '*(mx//3)+S)
#   for S in temp:
#     arr.append(S*3)
#   return arr

# N=int(input())
# print('\n'.join(pr(N)))
