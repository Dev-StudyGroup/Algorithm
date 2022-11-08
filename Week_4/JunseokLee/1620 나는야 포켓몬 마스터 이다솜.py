from collections import defaultdict
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    dic_num = defaultdict()
    dic_name = defaultdict()

    for i in range(1, N + 1):
        name = input().rstrip()
        dic_num[i] = name
        dic_name[name] = i

    for _ in range(M):
        value = input().rstrip()
        if value.isdigit():
            print(dic_num[int(value)])
        else:
            print(dic_name[value])
