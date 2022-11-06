N, K = map(int, input().split())
coins = []
answer = 0

for _ in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)

while K != 0:
    answer += K // coins[-1]
    K %= coins[-1]
    coins.pop()

print(answer)
