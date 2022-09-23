n = int(input())
words = set()
for i in range(n):
    words.add(input())

words = list(words)
words.sort()
words.sort(key = len)

for word in words:
    print(word)

