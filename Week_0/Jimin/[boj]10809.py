'''
'알파벳 찾기'
'''
S = input()
alpha_list = [-1] * 26
for i in range(len(S)):
    if alpha_list[ord(S[i])-97] == -1:
        alpha_list[ord(S[i]) - 97] = i

print(*alpha_list)