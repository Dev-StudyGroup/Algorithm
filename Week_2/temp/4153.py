"""
4153: 직각삼각형
"""
while True:
    tri = list(map(int, input().split()))
    if sum(tri) == 0:
        break
    tri.sort()
    if tri[0]**2 + tri[1]**2 == tri[2]**2:
        print("right")
    else:
        print("wrong")
