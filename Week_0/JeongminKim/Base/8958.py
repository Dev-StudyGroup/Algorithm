"""

    O가 문제를 맞은 것
    X가 문제를 틀린 것

    문제를 맞은 경우 그 문제의 점수는 연속된 O의 개수가 된다.

    풀이 방법
    연속적으로 풀이된 것을 알기 위해
    python list를 활용 맞힐때마다 append시켜줌

    입력
    첫쨰줄에는 테스트케이스의 개수
    그다음엔 각각의 테스트 케이스들

"""
n = int(input())
scores = []
answer = []
for _ in range(n):
    sols = input()
    score = 0
    answer = []
    for sol in sols:
        if sol == 'O':
            answer.append('O')
        else:
            answer = []
        score += len(answer)
    scores.append(score)

for i in range(n):
    print(scores[i])
