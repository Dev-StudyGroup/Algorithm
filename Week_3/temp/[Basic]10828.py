n = int(input())
commands = []
for _ in range(n):
    commands.append(input())

def performCommand(stack, command):
    command = command.split()
    length = len(stack)
    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if length == 0:
            return -1
        return stack.pop()

    elif command[0] == 'size':
        return length

    elif command[0] == 'empty':
        if length:
            return 0
        else:
            return 1

    elif command[0] == 'top':
        if length:
            return stack[-1]
        else:
            return -1

stack = []
for command in commands:
    result = performCommand(stack, command)
    if result is not None:
        print(result)