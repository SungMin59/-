N=int(input())
for i in range(N):
	star=""
	for k in range(N-i):
		star+=" "
	for k in range(i+1):
		star+="*"
	print(star)
