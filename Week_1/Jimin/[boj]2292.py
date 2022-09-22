'''
'벌집'
'''
N = int(input())

present = 1
idx = 1
if N != 1:
    while True:
        present += 6 * idx
        if N <= present:
            break
        idx += 1
    print(idx+1)
else:
    print(1)