"""

    첫쨰줄에는 테스트 케이스 개수 T
    각 테스트케이스의 반복횟수 R
    문자열 S가 공백으로 구분되어 주어짐
    [입력값 예제]
        T
        R S

    출력값:
        문자열 S를 입력받은 후 R번 반복해 새문자열 P만든후 출력


"""

T = int(input())
inputval = []
retval = []
def mkstring(R, S):
    R = int(R)
    return list(map(lambda x:x*R, S))
for _ in range(T):
    inputval.append(input().split())

for i in range(T):
    r, s = inputval[i]
    strings = mkstring(r,s)
    print(''.join(strings))