n, k = map(int, input().split())
data = [i for i in range(1, n+1)]

idx = 0
result = []
while data:
    length = len(data)
    idx = (idx + k - 1) % length
    result.append(str(data[idx]))
    data.remove(data[idx])

answer = ', '.join(result)
print("<" + answer + ">")