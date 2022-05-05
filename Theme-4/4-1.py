import sys

N = int(input())
inp = list(map(int, sys.stdin.readline().split()))
# 양심없는 날먹풀이
print(min(inp),max(inp))

# 문제 출제 의도 고려(인덱스 추가 질문시 풀이)

# mx,mn=-1000000,1000000
# for i in range(N):
#   if mx <= inp[i]:
#     mx = inp[i]
#   if mn >= inp[i]:
#     mn = inp[i]
# print(mn,mx)


# 정수 N제외 풀이(출제의도X)

# start = time.time()
# mx,mn=-1000000,1000000
# for i in inp:
#   if mx <= i:
#     mx = i
#   if mn >= i:
#     mn = i
# print(mn,mx)