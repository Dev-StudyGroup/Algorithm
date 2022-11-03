import heapq as hq

T = int(input())
for _ in range(T):
    k = int(input())
    deleted = [True] * k
    max_heap = []
    min_heap = []

    for i in range(k):
        operate, n = input().split()
        n = int(n)

        if operate == 'I':
            hq.heappush(max_heap, (-n, i))
            hq.heappush(min_heap, (n, i))
            deleted[i] = False
        if operate == 'D':
            if n == 1:
                while max_heap and deleted[max_heap[0][1]]:
                    hq.heappop(max_heap)
                if max_heap:
                    deleted[max_heap[0][1]] = True
                    hq.heappop(max_heap)
            else:
                while min_heap and deleted[min_heap[0][1]]:
                    hq.heappop(min_heap)
                if min_heap:
                    deleted[min_heap[0][1]] = True
                    hq.heappop(min_heap)

    while min_heap and deleted[min_heap[0][1]]:
        hq.heappop(min_heap)
    while max_heap and deleted[max_heap[0][1]]:
        hq.heappop(max_heap)

    if not min_heap or not max_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])
