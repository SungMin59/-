inp=[]
for i in range(10):
    inp.append(int(input()) % 42)
print(len(set(inp)))