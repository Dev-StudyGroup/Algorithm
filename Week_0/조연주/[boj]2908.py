"""
상수
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
def print_result(arr):
    for x in arr:
        print(x, end='')

a, b = input().split()

al = list(a)
bl = list(b)

ra = al[::-1]
rb = bl[::-1]

if ra[0] > rb[0]:
    print_result(ra)
elif ra[0] < rb[0]:
    print_result(rb)
else:
    if ra[1] > rb[1]:
        print_result(ra)
    elif ra[1] < rb[1]:
        print_result(rb)
    else:
        if ra[2] > rb[2]:
            print_result(ra)
        else:
            print_result(rb)
