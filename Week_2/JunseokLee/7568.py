N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

grade = []
for i in range(N):
    bigger = 1
    for j in range(N):
        if j == i:
            continue
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            bigger += 1
    grade.append(bigger)
print(*grade)