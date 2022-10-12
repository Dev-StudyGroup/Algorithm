'''
통계학

- 문제 요약
통계학에서 N개의 수를 대표하는 기본 통계값.(단, N은 홀수라고 가정하자)
    1. 산술평균: N개의 수들의 합을 N으로 나눈 값
    2. 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    3. 최빈값: N개의 수들 중 가장 많이 나타나는 값
    4. 범위: N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네가지 기본 통계값을 구하는 프로그램

- 입력 조건
첫째 줄에 수의 개수 N(1 <= N <= 500,000)이 주어짐. 단 N은 홀수.
그 다음 N개의 줄에 정수들이 주어짐. 
입력되는 정수의 절대값은 4000을 넘지 않는다.

- 출력 조건
첫째 줄에는 산술평균 출력. 소수점 이하 첫째 자리에서 반올림한 값을 출력.
둘째 줄에는 중앙값 출력.
셋째 줄에는 최빈값 출력. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값 출력.
넷째 줄에는 범위 출력.
'''
import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

# 산술평균
avg = sum(num)/n

# 반올림
if avg - int(avg) >= 0.5:
    avg = int(avg) + 1
elif avg - int(avg) <= -0.5:
    avg = int(avg) - 1
else:
    avg = int(avg)
print(avg)

# 중앙값
num.sort()
print(num[n//2])

# 최빈값
count_dict = {}
for i in num:
    if i not in count_dict.keys():
        count_dict[i] = 1
    else:
        count_dict[i] += 1
temp = [] # 최빈값 리스트
max_count = 1
for k, v in count_dict.items():
    if v > max_count:
        max_count = v
        temp = [k]
    elif v == max_count:
        temp.append(k)
if len(temp) == 1:
    print(temp[0])
else:
    print(temp[1])
     
# 범위
print(max(num)-min(num))