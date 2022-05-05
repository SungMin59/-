import sys

inp=[0]
while 1:
  try:
    inp.append(int(sys.stdin.readline().rstrip()))
  except:
    break
    
mx=max(inp)
print(mx,inp.index(mx),sep='\n')
