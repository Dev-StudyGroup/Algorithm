'''
'달팽이는 올라가고 싶다'
'''
A, B, V = map(int, input().split())
temp = V-A
answer = temp // (A-B) + 2
if temp % (A-B) == 0:
    answer -= 1

print(answer)