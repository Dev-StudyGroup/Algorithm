N = int(input())
words = set()

for _ in range(N):
    word = input()
    words.add(word)

words = list(words)
words.sort(key=lambda x: (len(x), x))
for word in words:
    print(word)
