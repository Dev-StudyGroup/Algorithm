'''
랜선 자르기

- 문제 요약
길이가 같은 N개의 랜선을 만들려고 한다.
K개의 길이가 제각각인 랜선을 갖고 있을때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램.

기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정.
이미 자른 랜선은 붙일 수 없음(ex. 300cm 짜리 랜선에서 140cm짜리 두개를 잘라내면 20cm는 버려야 함)
자를 때는 항상 센티미터 단위, 정수길이만큼 자른다고 가정.
N개보다 많이 만드는 것도 N개를 만드는 것에 포함됨

- 입력 조건
첫째 줄에는 이미 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N이 입력된다.
K는 1이상 10000이하의 정수이고, N은 1 이상 1,000,000이하의 정수.
항상 K <= N.
그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력됨.
랜선의 길이는 2^31-1보다 작거나 같은 자연수

- 출력 조건
첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력
'''
k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0 # 랜선 개수
    for l in lan:
        total += l // mid
    
    if total < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
