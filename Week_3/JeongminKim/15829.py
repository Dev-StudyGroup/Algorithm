"""

    해시 함수: 임의의 길이의 입력을 받아서 고정된 길이의 출력을 내보내는 함수이다.

    자료의 저장과 탐색

    a ~ z => 1 ~ 26
    abba => 1 2 2 1

    해시 값 계산 방법
        1. 문자열 혹은 수열을 하나의 정수로 치환
        2. 적당히 큰 수 M으로 나눠준다.
    문자열의 종류는 무한하지만, 출력범위는 정해져 있다. 그렇기 때문에 해시 충돌이 일어나고,
    해시 함수는 최대한 충돌이 적게 일어나야 한다.

    수열의 각 항마다 고유한 계수를 부여
    항의 번호에 해당하는 만큼 특정한 숫자를 거듭제곱해서 곱해준 다음 더한다.

    r 31
    M 1234567891
    입력
        1. 문자열의 길이 L
        2. 영문 소문자로만 이루어진 문자열 입력
        3. 모두 알파벳 소문자임

    math.pow() 사용하면 50점만 나오는 이유
    math.pow 는 IEEE754 부동소수점 표현 방법으로 매핑되어 있다보니 숫자가 커지면 overflow 가 발생

    def pow(__x: _SupportsFloatOrIndex, __y: _SupportsFloatOrIndex) -> float: ...

    float로 표현되기 때문에 범위가 넘어가는 경우에 overflow가 발생하게 된다.

"""


def cal(index, s):
    return (ord(s) - 96) * (31 ** index)


N = int(input())
M = 1234567891
line = input()
value = 0

for i in range(0, len(line)):
    value += cal(i, line[i])

value = value % M
print(int(value))
