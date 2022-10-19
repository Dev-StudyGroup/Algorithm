from collections import defaultdict


def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0] * (n + 1)
    parents = [i for i in range(n + 1)]
    dic = defaultdict()

    for i, e in enumerate(enroll):
        dic[e] = i + 1

    for i in range(n):
        if referral[i] == '-':
            parents[i + 1] = 0
        else:
            parents[i + 1] = dic[referral[i]]

    for i in range(len(seller)):
        find(parents, amount[i] * 100, dic[seller[i]], answer)
    return answer[1:]


def find(parents, money, number, answer):
    if parents[number] == number or money // 10 == 0:
        answer[number] += money
        return

    send = money // 10
    mine = money - send
    answer[number] += mine
    find(parents, send, parents[number], answer)
