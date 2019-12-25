'''
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
'''

C=int(input())
sum = 0
cnt = 0
allScore=[]
result=0

for i in range(C):
    score=list(map(int,input().split()))
    allScore.append(score)

for i in range(C):

    for j in range(1,len(allScore[i])):
        sum+=allScore[i][j]
    av=sum/allScore[i][0]


    for k in range(1,len(allScore[i])):
        if allScore[i][k]>av:
            cnt+=1

    result=cnt/(len(allScore[i])-1)*100
    print("%0.3f%%" %result)

    sum=0
    av=0
    cnt=0