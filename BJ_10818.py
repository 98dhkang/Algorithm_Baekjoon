N=input()

NN=list(map(int,input().split()))

Max=NN[0]
Min=NN[0]

for i in range(1,len(NN)):
    if NN[i]>Max:
        Max=NN[i]
    if NN[i]<Min:
        Min=NN[i]

print(Min, Max)