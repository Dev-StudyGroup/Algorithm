'''
'최댓값'
'''
max = 0
idx = -1
for i in range(9):
    num = int(input())
    if num > max:
        max = num
        idx = i+1

print(max)
print(idx)