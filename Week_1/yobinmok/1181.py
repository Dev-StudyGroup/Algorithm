n = int(input())
words = set()
for i in range(n):
    words.add(input())

words = list(words)
words.sort() # 사전순으로 정렬
words.sort(key = len) # 길이순으로 정렬

for word in words:
    print(word)

