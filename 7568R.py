
n=int(input())

whlist=[]

for i in range(n):
    weight,height=list(map(int,input().split()))
    whlist.append((weight,height))

for i in whlist:
    rank=1
    for j in whlist:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank, end=" ")