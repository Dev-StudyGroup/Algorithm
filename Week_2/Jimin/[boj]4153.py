'''
'직각삼각형'
'''
while True:
    array = list(map(int, input().split()))
    if array[0] == 0:
        break
    array.sort()
    for i in range(3):
        array[i] = array[i] * array[i]
    if array[0] + array[1] == array[2]:
        print("right")
    else:
        print("wrong")