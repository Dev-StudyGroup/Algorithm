# [BOJ] 1181 단어 정렬

n = int(input())
words = [input() for _ in range(n)]

words.sort(key=lambda x: (len(x), x))

for i in range(len(words)):
    if i == 0 or words[i-1] != words[i]:
        print(words[i])
        