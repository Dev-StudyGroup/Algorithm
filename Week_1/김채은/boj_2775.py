t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    apartment = [[0 for _ in range(n+1)] for _ in range(k+1)]

    for i in range(1, n+1):
        apartment[0][i] = i
    
    for i in range(1, k+1):
        for j in range(1, n+1):
            apartment[i][j] = sum(apartment[i-1][1:j+1])

    print(apartment[k][n])
    