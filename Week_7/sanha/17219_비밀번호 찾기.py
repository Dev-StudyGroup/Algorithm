import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
dic = defaultdict()

for _ in range(N):
    address, password = map(str, input().split())
    dic[address] = password

for _ in range(M):
    address = input().rstrip()
    print(dic[address])
    