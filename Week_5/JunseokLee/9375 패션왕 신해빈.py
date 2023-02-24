import sys
from collections import defaultdict

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        n = int(input())
        dic = defaultdict(list)
        clothes = set()
        num = []
        result = 1

        for _ in range(n):
            name, kind = input().split()
            clothes.add(kind)
            dic[kind].append(name)

        for c in clothes:
            result *= (len(dic[c]) + 1)

        print(result - 1)
