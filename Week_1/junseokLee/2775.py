T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())
    arr = [[i for i in range(1, n+1)]]+[[0 for _ in range(n)] for _ in range(k)]
    for a in range(1,k+1):
        for b in range(n):
            arr[a][b] += sum(arr[a-1][:b+1])
    print(arr[k][n-1])