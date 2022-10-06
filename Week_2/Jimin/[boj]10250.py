'''
'ACM 호텔'
'''
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        room = N // H
    else:
        room = N // H + 1

    floor = N - (room-1) * H

    if len(str(room)) == 1:
        room = str(0)+str(room)
    else:
        room = str(room)

    print(str(floor)+room)