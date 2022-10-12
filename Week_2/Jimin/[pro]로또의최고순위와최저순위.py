'''
'로또의 최고 순위와 최저 순위'
'''
def solution(lottos, win_nums):
    answer_range = 0
    same_cnt = 0
    for i in range(6):
        if lottos[i] == 0:
            answer_range += 1
        else:
            for j in range(6):
                if lottos[i] == win_nums[j]:
                    same_cnt += 1

    rank = 7 - same_cnt

    minimum_rank = rank
    maximum_rank = rank - answer_range
    if minimum_rank > 6:
        minimum_rank = 6
    if maximum_rank < 1:
        maximum_rank = 1
    elif maximum_rank > 6:
        maximum_rank = 6

    return [maximum_rank, minimum_rank]

print(solution([7, 8, 9, 10, 11, 12], [6, 5, 4, 3, 2, 1]))