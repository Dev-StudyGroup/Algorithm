N = int(input())
arr = []
for n in range(N):
    age, name = input().split()
    arr.append([age, name, n])
arr.sort(key=lambda x: (int(x[0]), x[2]))
for age, name, order in arr:
    print(age, name)
