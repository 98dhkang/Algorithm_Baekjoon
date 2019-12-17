#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

A=[]
B=[]

while(1):
    try:
        a,b=list(map(int,input().split()))
        A.append(a)
        B.append(b)
    except:
        break
i=0

while(1):
    if i<len(A):
        print(A[i]+B[i])
        i=i+1
    else :
        break