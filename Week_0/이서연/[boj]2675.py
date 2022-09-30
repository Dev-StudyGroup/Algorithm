'''
문자열 반복

- 문제 요약
문자열 S를 입력받은 후에 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램.
즉, 첫번째 문자를 R번 반복, 두번째 문자를 R번 반복하는 식으로 P를 만듦
S에는 QR Code "alphanumeric" 문자만 들어있음(0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:)

- 입력 조건
첫째 줄에 테스트 케이스의 개수 T(1<=T<=1000)가 주어짐.
각 테스트 케이스는 반복 횟수 R(1<=R<=8), 문자열 S가 공백으로 구분되어 주어짐.
S의 길이는 적어도 1이며, 20글자를 넘지 않음

- 출력 조건
각 테스트 케이스에 대해 P를 출력
'''
t = int(input())

for _ in range(t):
    r, s = input().split() # r, s는 string
    # for j in range(len(s)):
    #     print(s[j]*int(r), end='')
    # 아래처럼. 파이썬 문법에 익숙해지기
    for i in s:
        print(i * int(r), end = '')
    print()
