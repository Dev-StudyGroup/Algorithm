from collections import defaultdict
import math

def solution(enroll, referral, seller, amount):
    answer = []
    parentDict = dict(zip(enroll, referral))
    result = defaultdict(int)

    for i in range(len(seller)):
        value = amount[i] * 100
        target = seller[i]
        
        while 1:
            result[target] += math.ceil(value * 0.9)
            value = math.floor(value * 0.1)
            if parentDict[target] == '-':
                break
            if value < 1:
                result[target] += value
                break
            parent = parentDict[target]

            target = parent

    for s in enroll:
        answer.append(result[s])

    return answer