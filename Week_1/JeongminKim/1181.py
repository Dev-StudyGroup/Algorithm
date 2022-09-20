"""

    dict() 선언

    1. 단어의 길이 별로 정렬
    2. 단어의 길이가 같은 경우 알파벳 순으로 정렬

"""

word_dict = dict()

N = int(input())

for _ in range(N):
    word = input()
    length = len(word)

    if length not in word_dict.keys():
        word_dict[length] = [word]
    else:
        if word not in word_dict[length]:
            word_dict[length].append(word)
            word_dict[length] = sorted(word_dict[length], reverse=False)
word_dict = sorted(word_dict.items(), key=lambda item:item[0])
for length, word in word_dict:
    if len(word) == 1:
        print(word[0])
    else:
        for w in word:
            print(w)
