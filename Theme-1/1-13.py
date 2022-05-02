import sys
A, B = sys.stdin.readline().split()
A, B = map(int,A,B)
print(A*B[2],A*B[1],A*B[0],A*B,sep='\n')