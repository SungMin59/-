x = int(input())
i=0
while 1:
  if 3*i*(i+1)+1<=x<=3*(i+1)*(i+2)+1:
    break
  i+=1
if x!=1:
  print(i+2)
else:
  print(1)

# a,b=int(input()),1
# while a>1:a-=b*6;b+=1
# print(b)