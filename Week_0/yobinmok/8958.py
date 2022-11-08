n = int(input())
score = [0] * n
for i in range(n):
    count = 1
    test = input()
    ox = [0] * len(test)
    for j in range(len(test)):
        if test[j] == "O":
            ox[j] = count
            count += 1
        elif test[j] == "X":
            ox[j] = 0
            count = 1
    score[i] = sum(ox)

for i in range(n):
    print(score[i])