'''
OX퀴즈

- 문제 요약
OX퀴즈의 결과가 있음(O는 맞은 것, X는 틀린 것)
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수

ex) "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점

- 입력 조건
첫째 줄에 테스트 케이스의 개수가 주어짐.
각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보가 크고 80보다 작은 문자열.
(문자열은 O, X로만 이루어짐)

- 출력 조건
각 테스트 케이스마다 점수를 출력
'''
n = int(input())
for _ in range(n):
    str = input()
    score = 0
    count = 0 # 연속된 O의 개수
    for i in str:
        if i == 'O':
            score = score + 1 + count
            count = count + 1
        else:   # X 일때
            count = 0
    print(score)