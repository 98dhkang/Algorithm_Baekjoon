#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T=int(input())
sum=[]

for i in range(T):
    a,b=list(map(int,input().split()))
    sum.append(a+b)

for i in range(T):
    print("Case #"+str(i+1)+":",sum[i])
