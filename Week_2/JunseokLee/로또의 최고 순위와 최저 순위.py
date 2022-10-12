def rank(n):
    if n == 2:
        return 5
    elif n == 3:
        return 4
    elif n == 4:
        return 3
    elif n == 5:
        return 2
    elif n == 6:
        return 1
    return 6


def solution(lottos, win_nums):
    win = set(win_nums)
    cnt = 0
    zero = 0
    for n in lottos:
        if n == 0:
            zero += 1
            continue
        if n in win:
            cnt += 1

    answer = [rank(cnt + zero), rank(cnt)]
    return answer
