import sys
A, B = sys.stdin.readline().split()
A = int(A)
B = map(int,B)
print(A*B[2],A*B[1],A*B[0],A*B,sep='\n')