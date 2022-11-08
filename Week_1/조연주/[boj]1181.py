"""
단어 정렬
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = int(input())
words = []

for i in range(n):
    words.append(input())

words = list(set(words))
words.sort()
words.sort(key=lambda s: len(s))

print(*words, sep='\n')
