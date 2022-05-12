import sys
# 대략적인 구조/틀
sys.setrecursionlimit(10000)
    
N=int(input())
p=[0 for _ in range(N+1)]
rootlen=[0 for _ in range(N+1)]
tree=[[] for _ in range(N+1)]
rec=[False for _ in range(N+1)]
for i in range(N-1):
  pa,ch,li=map(int,sys.stdin.readline().split())
  tree[pa].append(ch)
  rootlen[ch]+=li

def dfs(n):
  rec[n]=True
  for nd in tree[n]:
    if rec[nd] == False:
      p[nd] = n
      rootlen[nd]+=rootlen[n]
    dfs(nd)

dfs(1)
arr=list(set(rootlen))
print(arr)
print(arr[-2]+arr[-1])