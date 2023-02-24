import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


if __name__ == "__main__":
    computer_num = int(input())
    network_num = int(input())
    parent = [0] * (computer_num + 1)
    for i in range(1, computer_num + 1):
        parent[i] = i

    for _ in range(network_num):
        a, b = map(int, input().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)

    count = 0
    for i in range(2, computer_num + 1):
        if find_parent(parent, i) == 1:
            count += 1
    print(count)
