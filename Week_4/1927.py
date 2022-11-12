"""
1927: 최소힙

최소힙이란 완전 이진 트리의 일종으로 여러 개의 값들 중 
최댓값이나 최솟값을 빠르게 찾아내도록 만들어진 자료구조이다.

* 루트노드의 인덱스 = 1
  왼쪽 자식 노드의 인덱스 = 부모 * 2
  오늘쪽 자식 노드의 인덱스 = 부모 * 2 + 1
  부모노드의 인덱스 = 자식 노드의 인덱스 // 2
"""
import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    calc = int(sys.stdin.readline())
    if calc == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, calc)
