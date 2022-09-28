"""

    주어진 직사각형 4분면으로 나눈다.

    0, 0, 10, 3

    가로 길이가 10
    세로 높이가 3

    x < 10/2 , y > 3/2 => 1 분면 => min(y-h, x-0)
    x < 10/2 , y < 3/2 => 2 분면 => min(y, x)
    x > 10/2 , y < 3/2 => 3 분면 => min(y, w-x)
    x > 10/2 , y > 3/2 => 4 분면 => min(h-y, w-x)


"""

def distance2line(x, y, w, h):
    """

    :param x, y: 현수의 위치
    :param w, h: 직사각형의 오른쪽 위 꼭짓점
    :return: 어떤 사분면에 위치하였는지
        위 주석 참고, return 1,2,3,4
    """

    center = (w/2, h/2)
    if x < center[0] and y > center[1]:
        return min(h-y, x)
    if x < center[0] and y <= center[1]:
        return min(y, x)
    if x >= center[0] and y <= center[1]:
        return min(y, w-x)
    if x >= center[0] and y > center[1]:
        return min(w-x, h-y)


x, y, w, h = map(int, input().split())
print(distance2line(x, y, w, h))