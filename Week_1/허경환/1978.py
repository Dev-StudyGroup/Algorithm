import math

#소수인지 체크하는 함수
def isprime(n):
    if n==1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

#입력
n = int(input())
ls=list(map(int, input().split()))
count=0
for i in ls:
    if isprime(i):
        count+=1
#출력
print(count)
