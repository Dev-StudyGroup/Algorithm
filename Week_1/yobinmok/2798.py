import sys
n, m = map(int, sys.stdin.readline().split()) # 카드의 개수, 목표 숫자
cards = list(map(int, sys.stdin.readline().split()))

case = []
for i in cards:
    for j in cards:
        for k in cards:
            if i != j and j != k and k != i:
                if i + j + k <= m:
                    case.append(i + j + k)

print(max(case))
