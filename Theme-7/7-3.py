# 121 123454321 12345654321
# 1 12321 123454321 1234567654321
 
a=int(input())
li=0
mx=0
while a > mx:
  li += 1
  mx += li

if a%2==1:
  m= mx - a + 1
  j= li - mx + a
else:
  m= li - mx + a
  j= mx - a + 1

# a=int(input())
# l= 0  
# mx = 0
# while a > mx:
#     l += 1  
#     mx += l
  
# g= (mx - a)
# if l % 2 == 0:
#     t= l - mx + a
#     u = mx - a + 1
# else :
#     t = mx - a + 1 
#     u = l + -mx + a
# print(f'{t}/{u}')


# import time
# a,b=int(input()),1
# def Sa(i):
#   return i*(2*i+1)
# def Sb(i):
#   return i*(2*i-1)

# start = time.time()

# bm,bj=0,0

# for i in range(a+1):
#   if Sa(i)< a < Sa(i+1):
#     if (Sa(i+1)-Sa(i))/2 < a-Sa(i):
#       bj=((Sa(i+1)-Sa(i))//2+1)-a+Sa(i)
#     else:
#       bj=a-Sa(i)
      
#   if Sb(i)< a < Sb(i+1):
#     if (Sb(i+1)-Sb(i))/2 < a-Sb(i):
#       bm=((Sb(i+1)-Sb(i))//2+1)-a+Sb(i)
#     else:
#       bm=a-Sb(i)
      
# # print(Sa(i),a,Sa(i+1)," ",i)
# print(str(bm)+"/"+str(bj))
# end = time.time()
# print(f"{end - start:.5f} sec")