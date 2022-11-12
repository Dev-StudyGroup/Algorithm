from math import factorial
#입력
n = int(input())
num = factorial(n)
count=0
while True:
    if num%10!=0:
        break
    else:
        count+=1
        num=num//10
#출력
print(count)
