arr=[]
for i in range(1,10001):
  arr.append( i+sum([int(j) for j in str(i)]) )
arr.sort()

nrr=list(set([int(p) for p in range(1,10001)]) - set(arr))
nrr.sort()
for k in nrr:
   print(k)

# li = [(i + sum(map(int, str(i)))) for i in range(1, 10001)]
# for i in range(1, 10001):
#     if i not in li:
#         print(i)