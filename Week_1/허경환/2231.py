#입력
n = int(input())

#문제유형파악 -> 브루트포스 구현

#분해합을 구하는 함수
def func(num):
    result=num
    for i in str(num):
        result+=int(i)
    return result

#분해합은 항상 생성자보다 크다.
for i in range(1,n+1):
    if func(i)==n:
        print(i)
        break
    if i==n:
        print(0)
