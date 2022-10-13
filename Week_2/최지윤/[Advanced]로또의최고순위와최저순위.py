def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    winning, zero = 0, 0

    for lotto in lottos:
        if lotto == 0:
            zero += 1
        elif lotto in win_nums:
            winning += 1

    answer.append(rank[winning+zero])
    answer.append(rank[winning])
    
    return answer