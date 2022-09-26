# [BOJ] 1920 수 찾기

from collections import defaultdict

n = int(input())
n_list = list(map(int, input().split()))
n_dict = defaultdict(int)

for number in n_list:
    n_dict[number] = 1

m = int(input())
m_list = list(map(int, input().split()))

for number in m_list:
    print(n_dict[number])