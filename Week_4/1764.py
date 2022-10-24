"""
1764: 듣보잡
* 집합과 리스트의 특성을 활용하는 문제
"""
# n: 들어보지 못한 사람, m: 보지 못한 사람
n, m = map(int, input().split())

notListen = set()
for _ in range(n):
    notListen.add(input())

notSee = set()
for _ in range(m):
    notSee.add(input())

notLS = sorted(list(notListen & notSee))

print(len(notLS))
for i in notLS:
    print(i)

    