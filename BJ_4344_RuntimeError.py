'''
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
'''

C=int(input())
sum = 0
cnt = 0
allScore=[]

for i in range(C):
    score=list(map(int,input().split()))
    allScore.append(score)

for i in range(0, C):

    for j in range(1, allScore[i][0] + 1):
        sum = sum + allScore[i][j]

    av = float(sum / allScore[i][0])

    for j in range(1, allScore[i][0] + 1):
        if (allScore[i][j] > av):
            cnt += 1
    result=cnt / allScore[i][0] * 100
    print("%.3f\%" %result)


