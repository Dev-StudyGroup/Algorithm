word = input().upper()
setWord = list(set(word))

cnt = []
for i in setWord:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    idx = cnt.index(max(cnt))
    print(setWord[idx])
