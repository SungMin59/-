N=int(input())
def pa(n):
  s=1
  if n>0:
    s= n * pa(n-1)
  return s

print(pa(N))