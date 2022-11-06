N = int(input())
p = list(map(int, input().split()))
p.sort()
times = [p[0]] * N

for i in range(1, N):
    times[i] = times[i - 1] + p[i]

print(sum(times))
