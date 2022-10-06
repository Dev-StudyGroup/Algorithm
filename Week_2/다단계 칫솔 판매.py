"""
Dev Matching: 다단계 칫솔 판매
"""
import math

def solution(enroll, referral, seller, amount):

    tree = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0 for _ in range(len(enroll))]))

    for i in range(len(seller)):
        earn = amount[i] * 100
        sell = seller[i]

        while True:
            if earn < 10:
                answer[sell] += earn
                break
            else:
                answer[sell] += math.ceil(earn * 0.9)
                if tree[sell] == '-':
                    break
                earn = math.floor(earn * 0.1)
                sell = tree[sell]

    print(list(answer.values()))
    return list(answer.values())
