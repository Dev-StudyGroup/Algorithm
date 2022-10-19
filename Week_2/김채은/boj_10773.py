k = int(input())

stack = []

for _ in range(k):
    number = int(input())

    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))
