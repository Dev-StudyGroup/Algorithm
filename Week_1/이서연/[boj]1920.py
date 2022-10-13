'''
수 찾기

- 문제 요약
N개의 정수 A[1], A[2], ..., A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램

- 입력 조건
첫째 줄에 자연수 N(1 <= N <= 100,000)이 주어짐. 다음 줄에는 N개의 정수 A[1], A[2], ..., A[N]이 주어짐.
다음 줄에는 M(1 <= M <= 100,000)이 주어짐. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -2**31 보다 크거나 같고 2**31보다 작다.

- 출력 조건
M개의 줄에 답을 출력. 존재하면 1, 존재하지 않으면 0 출력
'''
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start =  mid + 1  
    return None

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
for i in b:
    if binary_search(a, i, 0, n-1) != None:
        print(1)
    else:
        print(0)
