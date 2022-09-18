a = input()
alpha = []
for i in range(0,26):
    alpha.append(0)

for i in range(0, len(a)):
    code = ord(a[i])
    if code >= 97:
        code = code - 32
    idx = code - 65
    alpha[idx] += 1

max = 0 
for i in range(0, 26):
    if alpha[i] >= max:
        max = alpha[i]
        index = i

count = 0
for i in range(0, 26):
    if alpha[i] == max:
        count += 1

if count != 1:
    print("?")
else:
    print(chr(index + 65))

word = input().upper()
word_list = list(set(word))
cnt = []

for i in word_list:
  count = word.count(i)
  cnt.append(count)

if cnt.count(max(cnt)) >= 2:
  print("?")
else:
  print(word_list[(cnt.index(max(cnt)))])
