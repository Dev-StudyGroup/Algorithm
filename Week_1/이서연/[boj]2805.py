'''
나무 자르기

- 문제 요약
나무 M미터가 필요하다. 
절단기에 높에 H를 지정하여 높이가 H보다 큰 나무를 잘라서 적어도 M미터의 나무를 가져가기 위해 설정할 수 있는 높이의 최댓값을 구하는 프로그램.
높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.

- 입력 조건
첫째 줄에 나무의 수 N과 필요한 나무의 길이 M이 주어진다.
1 <= N <= 1,000,000
1 <= M <= 2,000,000,000
둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같다.
0 <= 높이 <= 1,000,000,000

- 출력 조건
적어도 M미터의 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 출력
'''
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree)
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in tree:
        if i > mid:
            total += i - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    sum = 0

print(result)
