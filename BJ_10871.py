#정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

N,X=list(map(int,input().split()))

Na=list(map(int,input().split()))

a=[]

for i in range(len(Na)):
    if (Na[i])<X:
        a.append(Na[i])

for i in range(len(a)):
    print(a[i])