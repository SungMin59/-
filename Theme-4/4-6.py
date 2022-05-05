import sys
N=int(sys.stdin.readline().rstrip())
def Sn(n):
  return n*(n+1)/2
  
inp=[]
for i in range(N):
  inp.append(sys.stdin.readline().rstrip())
  print(int(sum(map(lambda x:Sn(x.count("O")),(inp[i].split("X"))))))