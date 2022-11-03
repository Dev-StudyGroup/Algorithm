import heapq as hq

N = int(input())
ramens = []
q = []
for i in range(N):
    due, ramen = map(int, input().split())
    ramens.append((due, ramen))

ramens.sort()
for due, ramen in ramens:
    hq.heappush(q, ramen)
    if due < len(q):
        hq.heappop(q)
print(sum(q))
