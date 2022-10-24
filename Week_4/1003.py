"""
1003: 피보나치 함수
"""
zero = [1, 0]
one = [0, 1]

def fibonacci(n):
    leng = len(zero)
    if n >= leng:
        for i in range(leng, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])

t = int(input())

for i in range(t):
    fibonacci(int(input()))

"""
0 -> 1개
1 -> 1개
2 -> 1 0 (2개)
3 -> 2 1 1 0 (4개)
4 -> 3 2 2 1 1 0 1 0 (8개)
5 -> 4 3 2 2 1 1 0 1 0 3 2 1 1 0(14개)
6 -> 5 4
"""