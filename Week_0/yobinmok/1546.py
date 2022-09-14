n = int(input())
scores = list(map(int, input().split()))
max = max(scores)
sum = 0

for i in range(len(scores)):
    sum += (scores[i] / max) * 100

print(sum/n)