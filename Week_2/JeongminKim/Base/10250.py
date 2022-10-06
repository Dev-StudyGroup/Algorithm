"""

    손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호

    직사각형 모형

    각 층에 W개의 방이 있는 H층 건물이라고 가정

    엘레베이터는 가장 왼쪽에 있다.

    방 호수는 YYXX, YXX => Y층 XX호이다.

    ex
    102 보다 301를 더 선호한다.
        => 그 이유는 102호는 2, 301호는 1만큼걷기떄문에 더 선호한다.
    걷는 거리가 같을 때에는 아랫층의 방을 더 선호함

"""

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    num = N // H + 1
    floor = N % H

    if floor == 0:
        num = N // H
        floor = H

    room = floor * 100 + num

    print(room)
