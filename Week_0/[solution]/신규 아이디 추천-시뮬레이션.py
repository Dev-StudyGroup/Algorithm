"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 신규 아이디 추천
description : 시뮬레이션
"""

from typing import Final


def solution(newId):
    HYPHEN: Final = "-"
    UNDER_LINE: Final = "_"
    FULL_STOP: Final = "."
    CHECK_LENGTH_NUM: Final = 0
    LAST_NUM: Final = -1
    MAX_LENGTH_NUM: Final = 15
    MIN_LENGTH_NUM: Final = 2
    ALPHABET_A: Final = "a"

    answer = ""
    lowerNewId = newId.lower()

    for splitId in lowerNewId:
        if splitId.isalnum() or splitId in [HYPHEN, UNDER_LINE]:
            answer += splitId
        elif splitId == FULL_STOP:
            if len(answer) == CHECK_LENGTH_NUM:
                continue
            elif answer[LAST_NUM] != splitId:
                answer += splitId

    if len(answer) != CHECK_LENGTH_NUM and answer[LAST_NUM] == FULL_STOP:
        answer = answer[:LAST_NUM]
    if len(answer) == CHECK_LENGTH_NUM:
        answer += ALPHABET_A
    elif len(answer) > MAX_LENGTH_NUM:
        answer = answer[:MAX_LENGTH_NUM]
        if answer[LAST_NUM] == FULL_STOP:
            answer = answer[:LAST_NUM]

    while len(answer) <= MIN_LENGTH_NUM:
        answer += answer[LAST_NUM]

    return answer


if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))
