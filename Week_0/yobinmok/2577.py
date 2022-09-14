n = [] # [0] * 10 -> 초기화하는 방법
for i in range(10):
    n.append(0)

result = str(int(input()) * int(input()) * int(input()))
for i in result:
    n[int(i)] += 1

for i in n:
    print(i)