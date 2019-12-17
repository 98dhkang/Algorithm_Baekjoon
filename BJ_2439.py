N=int(input())

star="*"

for i in range(N-1,-1,-1):
    print(" "*i,end="")
    print("*"*(N-i))
