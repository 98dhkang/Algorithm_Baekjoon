'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''

N=int(input())
Nlist=[]

for i in range(N):
    a=int(input())
    Nlist.append(a)

Nlist.sort()

for i in range(len(Nlist)):
    print(Nlist[i])