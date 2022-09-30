num = int(input())
n = []
word = []
for i in range(num):
    temp = input().split()
    n.append(int(temp[0]))
    word.append(temp[1])

for i in range(num):
    for j in word[i]:
        print(j * n[i], end="")
    print()