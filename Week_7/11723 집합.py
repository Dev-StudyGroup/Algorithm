import sys

input = sys.stdin.readline

if __name__ == "__main__":
    M = int(input())
    numbers = [0] * 21
    for _ in range(M):
        command = input().split()
        if command[0] == "add":
            numbers[int(command[1])] = 1

        elif command[0] == "remove":
            numbers[int(command[1])] = 0

        elif command[0] == "check":
            print(numbers[int(command[1])])

        elif command[0] == "toggle":
            if numbers[int(command[1])]:
                numbers[int(command[1])] = 0
                continue
            numbers[int(command[1])] = 1

        elif command[0] == "all":
            numbers = [1] * 21

        elif command[0] == "empty":
            numbers = [0] * 21
