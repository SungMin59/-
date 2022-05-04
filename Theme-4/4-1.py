import sys
N=int(input())
inp = [x for x in map(int,sys.stdin.readline().rstrip().split())]
max = inp[0]
min = inp[0]

for i in inp[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)​
