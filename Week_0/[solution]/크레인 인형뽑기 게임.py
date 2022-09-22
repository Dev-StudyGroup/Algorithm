"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 크레인 인형뽑기 게임
description : 구현
"""

from typing import Final


def solution(board, moves):
    INIT_NUMBER: Final = 0
    CHECK_NUMBER: Final = 0
    ADD_NUMBER: Final = 2

    answer = INIT_NUMBER
    stack = []

    for i in moves:
        result = 0

        for j in range(len(board)):
            if board[j][i - 1] != CHECK_NUMBER:
                result = board[j][i - 1]
                board[j][i - 1] = INIT_NUMBER
                break

        if result == CHECK_NUMBER:
            continue
        if not stack:
            stack.append(result)
        else:
            last = stack.pop()

            if last == result:
                answer += ADD_NUMBER
            else:
                stack.append(last)
                stack.append(result)

    return answer


if __name__ == "__main__":
    print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                   [1, 5, 3, 5, 1, 2, 1, 4]))
