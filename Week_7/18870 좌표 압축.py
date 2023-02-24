import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    array = list(set(numbers))
    array.sort()
    dic = dict()
    for i in range(len(array)):
        dic[array[i]] = i

    for number in numbers:
        print(dic[number], end=" ")
