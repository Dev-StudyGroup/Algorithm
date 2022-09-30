S=input()
alpha=[-1]*26
for i in range(len(S)):
    alpha[ord(S[i])-97] = S.index(S[i])
print(*alpha)