a=input()
for i in range(97,123):
  print(a.find(chr(i)),end=' ')

# print(*map(input().find,map(chr,range(97,123))))