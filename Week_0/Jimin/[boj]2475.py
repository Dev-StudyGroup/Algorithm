'''
'검증수'
'''
num = list(map(int, input().split()))
for i in range(5):
    num[i] = num[i]**2
print(sum(num)%10)