'''
'단어 공부'
'''
string = input()
string = string.upper()

alpha_dic = {}
for i in string:
    if i in alpha_dic:
        alpha_dic[i] += 1
    else:
        alpha_dic[i] = 1

alpha_dic = sorted(alpha_dic.items(), key=lambda x:x[1], reverse=True)
if len(alpha_dic) == 1 or alpha_dic[0][1] != alpha_dic[1][1]:
    print(alpha_dic[0][0])
else:
    print("?")
