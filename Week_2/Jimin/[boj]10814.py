'''
'나이순 정렬'
'''
import heapq

N = int(input())
member = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    heapq.heappush(member, [age, i, name])

while len(member) != 0:
    a, b, c = heapq.heappop(member)
    print(a, c)