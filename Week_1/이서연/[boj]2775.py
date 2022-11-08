'''
부녀회장이 될테야

- 문제 요약
아파트 거주 조건 "a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다"
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정할때, 주어지는 k와 n에 대해 k층에 n호에는 몇명이 살고 있는지 출력.
단, 아파트에는 0층부터 있고, 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

- 입력 조건
첫째 줄에 Test case의 수 T가 주어진다.
각각의 케이스마다 첫번째 줄에 정수 k, 두번째 줄에 정수 n이 주어진다.
1 <= k,n <= 14

- 출력 조건
각각의 Test case에 대해 해당 집 거주민 수를 출력
'''
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    count = [i for i in range(1,n+1)] # 1호부터 n호까지 거주민 수
    for x in range(1, k): # k-1층의 거주민수 구하기
        down_count = count
        count = []
        for y in range(n):
            count.append(sum(down_count[:y+1]))

    print(sum(count[:n]))
