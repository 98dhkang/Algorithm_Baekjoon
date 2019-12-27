'''
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
'''

T = int(input())

Result = []
Result.insert(0,0)
Result.insert(1,1)
Result.insert(2,2)
Result.insert(3,4)

for i in range(T):
    n=int(input())
    for j in range(4,n+1):
        Result.insert(j,Result[j-1]+Result[j-2]+Result[j-3])
    print(Result[n])


