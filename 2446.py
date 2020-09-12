#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.


n = int(input())
mylist=[]

num=1

for i in range(n):
    str=" "*i + "*"*(2*n-num-i)
    mylist.append(str)
    num+=1

num=-2

for i in range(n-1):
    str2 = " " * (n-i-2) + "*" * (n+num)
    mylist.append(str2)
    num += 2
for i in range(n*2-1):
    print(mylist[i])