testCase = int(input())
for _ in range(testCase):
    h, w, n = map(int, input().split())
    roomNum = n // h + 1
    floor = n % h
    if n % h == 0:
        roomNum = n // h
        floor = h
    room = floor * 100 + roomNum
    print(room)