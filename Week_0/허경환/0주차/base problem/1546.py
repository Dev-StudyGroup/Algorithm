#입력
n = int(input())
score = list(map(int, input().split()))

#구현
m = max(score)
for i in range(len(score)):
    score[i]=(score[i]/m)*100

result=sum(score)/n

#출력
print(result)
