"""

    재현이는 잘못된 수를 부를때마다 0을 외침

    가장 최근에 재민이가 쓴 수를 지우게 시킨다.

    재민이는 모든 수를 받아 적은 후 그 수의 합을 알고싶다.

    첫 번째 줄에는 정수 K가 주어진다.

    정수가 0일 경우에는 가장 최근에 쓴수를 지우고 아닐경우 해당 수를 쓴다.

    정수가 0일 경우 지울 수 있는 수가 있음을 보장한다.

"""
K = int(input())

num = []

for _ in range(K):
    n = int(input())
    if n != 0:
        num.append(n)
    else:
        num.pop(-1)

print(sum(num))