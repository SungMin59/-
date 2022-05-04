N=input()
if int(N)<10:
  N="0"+str(N)
T=N
c=0

while 1:
  N=N[-1]+str(sum(list(map(int,N)))%10)
  c+=1
  if T==N:
    break
print(c)