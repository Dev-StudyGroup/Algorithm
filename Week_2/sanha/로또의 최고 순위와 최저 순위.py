def find_correct(lottos, win_nums):
    cnt = 0
    for lotto in lottos:
        if lotto == 0:
            continue
        for win_num in win_nums:
            if lotto == win_num:
                cnt += 1
                break
    return cnt

def solution(lottos, win_nums):
    answer = []
    zeros = lottos.count(0)
    cnt = find_correct(lottos, win_nums)
    min_rank = (6 - cnt) + 1
    if min_rank > 6:
        min_rank = 6
    max_rank = (6 - cnt - zeros) + 1
    if max_rank > 6:
        max_rank = 6
    answer.append(max_rank)
    answer.append(min_rank)
    return answer
