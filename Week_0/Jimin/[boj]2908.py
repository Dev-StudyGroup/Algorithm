'''
'상수'
'''
A, B = map(int, input().split())
def reverse(x):
    x = str(x)
    new_x = x[2]+x[1]+x[0]
    return int(new_x)

new_A = reverse(A)
new_B = reverse(B)

print(max(new_A, new_B))