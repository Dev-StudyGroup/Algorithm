'''
'단어 정렬'
'''
N = int(input())
eng_dic = {}
for i in range(N):
    word = input()
    if word in eng_dic:
        continue
    else:
        eng_dic[word] = len(word)

eng_dic = dict(sorted(eng_dic.items(), key=lambda x:x[0]))
eng_dic = dict(sorted(eng_dic.items(), key=lambda x:x[1]))

for i in eng_dic:
    print(i)