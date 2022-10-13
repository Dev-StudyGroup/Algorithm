"""

    PS => 두 개의 괄호 기호 '(' 와 ')' 으로 구성되어 있는 문자열이다.

    VPS => 괄호의 모양이 바르게 구성된 문자열 (())

    두 VPS x와 y 접합시킨 새로운 문자열 xy도 VPS이다.

"""


def check_vps(s):
    answer = True

    # 여는 괄호를 담는 stack
    open_bracket = []
    for i in s:
        if i == '(':
            open_bracket.append(i)
        else:
            if len(open_bracket) == 0:
                return False
            else:
                open_bracket.pop(-1)
    if len(open_bracket) > 0:
        return False
    return answer


N = int(input())

for _ in range(N):

    PS = input().split()

    result = list(map(check_vps, PS))
    r = result[0]
    for i in range(1, len(result)):
        r = result[i] and r

    if r:
        print("YES")
    else:
        print("NO")

