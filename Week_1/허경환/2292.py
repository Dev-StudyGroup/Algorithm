#입력
n = int(input())

#문제유형파악 -> 1, 6*2-6, 6*3-6, 6*4-6, ....

temp=1
answer=0
for i in range(1, n+1):
    temp+=6*i-6
    if n <= temp:
        answer=i
        break

#출력
print(answer)
