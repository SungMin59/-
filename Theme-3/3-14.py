N=input()
if int(N)<10:
  N="0"+str(N)
  print(N)
while 1:
  try:
    N=sum(list(map(int,N)))
    print(N)
  except:
    break