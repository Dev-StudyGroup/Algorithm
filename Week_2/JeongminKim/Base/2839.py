"""

    문제 설명

    상근이는 설탕을 정확하게 N킬로그램 배달해야함

    봉지에는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

    최대한 적은 봉지를 가지고 가야한다.

    BruteForce

"""

N = int(input())

cnt = 9999999
flag = 0
for i in range(0, N // 5 + 1):
    for j in range(0, (N - (5 * i)) // 3 + 1):
        sugar = 5 * i + 3 * j
        c = i + j
        if N == sugar:
            flag = 1
            if cnt > c:
                cnt = c

if not flag:
    print("-1")
else:
    print(cnt)
