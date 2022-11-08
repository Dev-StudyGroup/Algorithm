"""
음계
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
nums = list(map(int, input().split()))

if nums == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif nums == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")
        