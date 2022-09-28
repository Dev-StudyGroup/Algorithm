'''
음계

- 문제 요약
다장도는 c d e f g a b C, 총 8개 음으로 이루어짐.
문제에서 8개 음은 숫자로 바꾸어 표현(c는 1, d는 2, ...)
1부터 8까지 차례대로 연주하면 ascending,
8부터 1까지 차례대로 연주하면 descending,
둘 다 아니라면 mixed

연주한 순서가 주어졌을때, 이를 판별하는 프로그램

- 입력 조건
첫째 줄에 8개 숫자가 주어짐. 1부터 8까지 숫자가 한번씩

- 출력 조건
첫째 줄에 ascending, descending, mixed 중 하나를 출력
'''
a = list(map(int, input().split()))

check = True # 순서대로 맞는지 확인
rev = False # 역순인지 확인
if (a[0]==8):
    a.reverse()
    rev = True
for i in range(8):
    if a[i] != i + 1:
        check = False
        break
if check:
    if rev:
        print('descending')
    else:
        print('ascending')
else:
    print('mixed')

a = list(map(int, input().split()))
 
# for문 사용하지 않고 두 리스트 비교하는 방법이 더 간단
# if a == sorted(a):
#     print('ascending')
# elif a == sorted(a, reverse=True):
#     print('descending')
# else:
#     print('mixed')