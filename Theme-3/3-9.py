N=int(input())
star=""
for i in range(N):
	for k in range(i+1):
		star+="*"
	print(star)
'''
for i in range(N):
	print((i+1)*'*')
'''
