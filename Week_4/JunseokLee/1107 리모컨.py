if __name__ == "__main__":
    N = int(input())
    M = int(input())
    res = abs(100 - N)
    if M:
        not_worked = set(input().split())
    else:
        not_worked = set()

    for i in range(1000001):
        for n in str(i):
            if n in not_worked:
                break
        else:
            res = min(res, len(str(i)) + abs(i - N))

    print(res)
