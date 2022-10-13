'''
'이항 계수 1'
'''

N, K = map(int, input().split())

num1 = 1
num2 = 1
for i in range(K):
    num1 = num1 * N
    N -= 1

    num2 = num2 * K
    K -= 1

print(num1 // num2)
