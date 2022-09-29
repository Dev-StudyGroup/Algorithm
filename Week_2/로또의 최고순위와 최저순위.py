"""
Dev Matching: 로또의 최고순위와 최저순위
"""
def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    same = 0; zero = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            same += 1

    answer = rank[same + zero], rank[same]
    return answer
