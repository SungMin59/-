import sys
sys.setrecursionlimit(100000)
N=int(input())
p = [0 for _ in range(N+1)]
rec = [False for _ in range(N+1)]
tree = [[] for _ in range(N+1)]

def f(n):
  rec[n]=True
  for nd in tree[n]:
    if rec[nd] == False:
      p[nd] = n
      f(nd)
for _ in range(N-1):
	a,b = map(int,sys.stdin.readline().split())
	tree[a].append(b)
	tree[b].append(a)
f(1)
for i in range(2, N+1):
    print(p[i])