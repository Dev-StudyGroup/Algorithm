"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 키패드 누르기
description : 구현
"""

from typing import Final


def solution(numbers, hand):
    INIT_LEFT_X: Final = 3
    INIT_LEFT_Y: Final = 0
    INIT_RIGHT_X: Final = 3
    INIT_RIGHT_Y: Final = 2

    CHECK_LEFT: Final = [1, 4, 7]
    CHECK_RIGHT: Final = [3, 6, 9]
    CHECK_RIGHT_HAND: Final = "right"

    ADD_LEFT: Final = "L"
    ADD_RIGHT: Final = "R"

    FROM_COORD_TO_KEYPAD: Final = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                                   4: [1, 0], 5: [1, 1], 6: [1, 2],
                                   7: [2, 0], 8: [2, 1], 9: [2, 2],
                                   0: [3, 1]}

    leftX, leftY, rightX, rightY = INIT_LEFT_X, INIT_LEFT_Y, INIT_RIGHT_X, INIT_RIGHT_Y
    answer = ""

    for number in numbers:
        if number in CHECK_LEFT:
            answer += ADD_LEFT
            leftX, leftY = FROM_COORD_TO_KEYPAD[number]
        elif number in CHECK_RIGHT:
            answer += ADD_RIGHT
            rightX, rightY = FROM_COORD_TO_KEYPAD[number]
        else:
            distLeft = abs(leftX - FROM_COORD_TO_KEYPAD[number][0]) + abs(leftY - FROM_COORD_TO_KEYPAD[number][1])
            distRight = abs(rightX - FROM_COORD_TO_KEYPAD[number][0]) + abs(rightY - FROM_COORD_TO_KEYPAD[number][1])

            if distLeft > distRight:
                answer += ADD_RIGHT
                rightX, rightY = FROM_COORD_TO_KEYPAD[number]
            elif distLeft < distRight:
                answer += ADD_LEFT
                leftX, leftY = FROM_COORD_TO_KEYPAD[number]
            else:
                if hand == CHECK_RIGHT_HAND:
                    answer += ADD_RIGHT
                    rightX, rightY = FROM_COORD_TO_KEYPAD[number]
                else:
                    answer += ADD_LEFT
                    leftX, leftY = FROM_COORD_TO_KEYPAD[number]

    return answer


if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
