'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.


'''

T=int(input())

b=[]
numlist=[]
stlist=[]

for i in range(T):
    a=list(map(str,input().split()))
    b.append(a)

#print(b)

for i in range(T):
    num=b[i][0]
    numlist.append(num)

for i in range(T):
    st=b[i][1]
    stlist.append(st)

for i in range(T):
    for j in range(len(stlist[i])):
        print(stlist[i][j]*int(numlist[i]),end="")
    print()