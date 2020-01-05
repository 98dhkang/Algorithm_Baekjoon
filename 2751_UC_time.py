'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''

N=int(input())

alist=[]

for i in range(N):
    a=int(input())
    alist.append(a)

alist.sort()

for i in range(N):
    print(alist[i])