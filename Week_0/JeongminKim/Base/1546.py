"""

    M : 점수 중 최댓값
    모든 점수를 점수 / M * 100으로 고친다.

    출력 값 새로운 평균을 출력


"""

cnt = int(input())
scores = list(map(int, input().split()))


def solution(cnt, subject):

    if len(subject) != cnt:
        return 0
    M = max(subject)

    subject = list(map(lambda x: x / M * 100, subject))

    return sum(subject) / cnt


mean_score = solution(cnt, scores)
print(mean_score)



