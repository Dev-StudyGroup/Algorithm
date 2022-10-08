'''
덩치

- 문제 요약
학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력하는 프로그램.
덩치는 (몸무게, 키)로 표현.
두 사람 A와 B의 덩치가 각각 (x,y), (p,q)라고 할 때, x>p, y>q이면 A의 덩치가 B의 덩치보다 크다고 한다.
키, 몸무게가 둘다 크지 않으면 크기를 누가 더 크다고 말할 수 없다.
덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수가 k명이라면 k+1이 된다.
같은 덩치 등수를 가진 사람이 여러 명일 수 있다.

- 입력 조건
첫째 줄에는 전체 사람의 수 N이 주어진다.
둘째 줄부터 N 줄에 걸쳐서 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 주어진다.
2 <= N <= 50
10 <= x,y <= 200

- 출력 조건
나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력.(공백 문자로 구분)
'''
n = int(input())
bulk = []
for _ in range(n):
    bulk.append(list(map(int, input().split())))

count = [0]*n # 자신보다 큰 사람 카운트

for i in range(n):
    for j in range(i+1, n):
        if bulk[i][0] > bulk[j][0]:
            if bulk[i][1] > bulk[j][1]:
                count[j] += 1
        
        elif bulk[i][0] < bulk[j][0]:
            if bulk[i][1] < bulk[j][1]:
                count[i] += 1

for x in count:
    print(x+1, end=' ')
