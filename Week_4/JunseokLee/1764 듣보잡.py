if __name__ == "__main__":
    N, M = map(int, input().split())
    name = set()
    for _ in range(N):
        name.add(input())
    arr =[]
    for _ in range(M):
        not_see_name = input()
        if not_see_name in name:
            arr.append(not_see_name)
    arr.sort()
    print(len(arr))
    for reduplication in arr:
        print(reduplication)
