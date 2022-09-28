N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
arr1 = set(arr1)
for num in arr2:
    if num in arr1:
        print(1)
    else:
        print(0)