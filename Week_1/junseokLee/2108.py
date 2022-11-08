N = int(input())
arr = []
arr1 = [0] * 8001
num = set()
for _ in range(N):
    n = int(input())
    arr.append(n)
    if n not in num:
        num.add(n)
    arr1[4000 + n] += 1

print(round(sum(arr) / N))
arr.sort()
print(arr[len(arr) // 2])

maximum = -1
temp = []
for i in range(8001):
    if arr1[i] < maximum:
        continue
    elif arr1[i] > maximum:
        maximum = arr1[i]
        temp = []
        temp.append(i-4000)

    elif arr1[i] == maximum:
        temp.append(i-4000)
temp.sort()
if len(temp)>1:
    print(temp[1])
else:
    print(temp[0])

print(max(arr) - min(arr))
