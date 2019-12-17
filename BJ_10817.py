#세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

A,B,C=list(map(int,input().split()))

if (A>=B) & (A<=C):
    print(A)
elif (A>=C) & (A<=B):
    print(A)
elif (B>=C) & (B<=A):
    print(B)
elif (B>=A) & (B<=C):
    print(B)
elif (C>=A) & (C<=B):
    print(C)
elif (C>=B) & (C<=A):
    print(C)