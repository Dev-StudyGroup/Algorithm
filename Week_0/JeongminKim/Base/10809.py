"""

    ascii 97~122 a~z

"""

alpha = dict()
for i in range(97, 123):
    alpha[chr(i)] = -1

sentence = input()

for i in range(len(sentence)):
    if alpha[sentence[i]] == -1:
        alpha[sentence[i]] = i

print(" ".join(list(map(str,alpha.values()))))
