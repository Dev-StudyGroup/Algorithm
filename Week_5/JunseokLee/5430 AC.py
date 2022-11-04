import sys
from collections import deque

input = sys.stdin.readline


def input_commands(commands, num):
    reverse_count = 0
    for command in commands:
        if command == 'R':
            reverse_count += 1
        elif command == 'D':
            if not num:
                return True

            if reverse_count % 2:
                q.pop()
            else:
                q.popleft()
            num -= 1

    if reverse_count % 2:
        q.reverse()
    return False


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        commands = " ".join(input().rstrip()).split()
        num = int(input())
        q = deque(input().lstrip('[').rstrip(']\n').split(','))
        if not num:
            q = []
        if input_commands(commands, num):
            print("error")
            continue
        print('[' + ",".join(q) + ']')
