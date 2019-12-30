'''
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
'''

N=str(input())
Nlist=[]

for i in range(len(N)):
    Nlist.append(int(N[i]))

Nlist.sort()

for i in range(len(Nlist)-1,-1,-1):
    print(Nlist[i],end="")