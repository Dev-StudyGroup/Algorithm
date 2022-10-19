n, k = map(int, input().split())

numbers = [1 for _ in range(n+1)]
answer = []

count = 1
while len(answer) < n:
    for i in range(1, n+1):
        if not numbers[i]:
            continue
        if count < k:
            count += 1
        elif count == k:
            answer.append(str(i))
            numbers[i] = 0
            count = 1

print('<'+', '.join(answer)+'>')
