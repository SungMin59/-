import time
a,b=int(input()),1
def Sa(i):
  return 2*i*(i+1)
def Sb(i):
  return 2*i*(i-1)
  
start = time.time()

for i in range(a+1):
  if Sa(i)< a < Sb(i):
    print(Sa(i),a,Sb(i))
    

end = time.time()
print(f"{end - start:.5f} sec")