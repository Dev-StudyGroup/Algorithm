"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 신규 아이디 추천
description : 파싱, 정규식
"""

from re import sub

def solution(newId):
    answer = newId.lower()
    answer = sub("[^a-z0-9-_.]", "", answer)
    answer = sub("\.+", ".", answer)
    answer = sub("(^\.|\.$)", "", answer)
    answer = answer if answer else "a"
    answer = sub("\.$", "", answer[:15])
    answer = answer if len(answer) > 3 else answer + answer[-1] * (3 - len(answer))

    return answer

if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))