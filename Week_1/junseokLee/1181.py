N = int(input())
words = []
for n in range(N):
    s = input()
    words.append([s, len(s)])

words.sort(key=lambda x: (x[1], x[0]))
result = []
for i in range(len(words)):
    result.append(words[i][0])
print(result[0])
for i in range(1, len(result)):
    if result[i - 1] == result[i]:
        continue
    print(result[i])
