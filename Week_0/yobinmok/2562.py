n = []
for i in range(9):
    n.append(int(input()))

max = 0 # max함수 이용해도 됨
for i in range(9):
    if n[i] > max:
        max = n[i]
        index = i + 1

print(max)
print(index) # a.index(max) + 1