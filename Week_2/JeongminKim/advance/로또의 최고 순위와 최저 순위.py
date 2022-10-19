"""
    로또 6/45 => 1부터 45까지의 숫자 중 6개를 찍어서 맞치는 대표적인 복권

    6개 번호가 모두 일치 > 1
    5개 번호가 일치 > 2
    4개 번호가 일치 > 3
    3개 번호가 일치 > 4
    2개 번호가 일치 > 5
    그외 > 6 ===> 1개 번호만 일치하거나 , 하나도 맞추지 못할경우

    알아볼 수 없는 번호 => 0으로 표기

    순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다. 

    민우가 구매한 로또 번호가 담긴 배열 => lottos
    당첨 번호를 담은 배열 => win_nums
    당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return

    win_nums의 원소들은 2개 이상 담겨있지 않습니다.

"""


def get_score(lotto, win_num):
    """일치하는 번호의 개수를 score라 하고 score를 얻는 함수"""
    score = 0
    for num in lotto:
        if num in win_num:
            score += 1

    return score


def get_rank(score):
    """ score에 맞는 rank를 return 하는 함수"""
    rank_board = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6}
    rank = 0
    if score <= 1:
        score = 1
    rank = rank_board[score]
    return rank


def get_possible_score(lotto, score):
    """ 가능한 최고 점수 """
    zero_count = lotto.count(0)
    return score + zero_count


def solution(lottos, win_nums):
    """ solution, 얻을 수 있는 최고 rank와 최저 rank 구하기 """
    answer = []

    lowest_score = get_score(lottos, win_nums)
    lowest_rank = get_rank(lowest_score)
    highest_rank = get_rank(get_possible_score(lottos, lowest_score))
    answer.append(highest_rank)
    answer.append(lowest_rank)

    return answer


if __name__ == '__main__':
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # > [3, 5]
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])) # > [1, 6]
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])) # [1, 1]
