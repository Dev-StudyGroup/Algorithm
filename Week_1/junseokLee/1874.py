n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
index = 1
result = []
temp=[]
for i in range(n):
    while arr[i] >= index:
        result.append('+')
        stack.append(index)
        index += 1
    else:
        if len(stack):
            temp.append(stack.pop())
        result.append('-')

if temp == arr:
    for i in range(len(result)):
        print(result[i])
else:
    print("NO")