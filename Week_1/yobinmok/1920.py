import sys

def search(arr, k):
    L = 0; R = len(arr) - 1
    while L <= R:
        mid = (L + R) // 2
        if k < arr[mid]:
            R = mid - 1
        elif k > arr[mid]:
            L = mid + 1
        else:
            return "1"
    return "0"

n = int(sys.stdin.readline())
nums1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))
nums1.sort()

for num in nums2:
    print(binary(nums1, num))