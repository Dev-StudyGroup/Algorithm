from collections import defaultdict
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    dic = defaultdict(list)
    for _ in range(N):
        address, password = input().rstrip().split()
        dic[address] = password
    for _ in range(M):
        address = input().rstrip()
        print(dic[address])
