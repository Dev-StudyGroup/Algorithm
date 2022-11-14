"""

    듣도 못한 사람의 수 N
    보도 못한 사람의 수 M

    듣도 보도 못한 사람을 출력 하라

"""
from collections import defaultdict
N, M = map(int, input().split())

# 듣도 못한 사람
no_listen = defaultdict(list)
# 듣보잡인 사람
result = []
for _ in range(N):
    name = input()
    no_listen[name] = 1

for _ in range(M):
    name = input()
    if no_listen[name]:
        result.append(name)
print(len(result))
print('\n'.join(sorted(result, reverse=False)))
