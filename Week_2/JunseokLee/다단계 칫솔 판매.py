def solution(enroll, referral, seller, amount):
    result = [0] * len(enroll)
    dic = dict()
    for i in range(len(enroll)):
        dic[enroll[i]] = i
    for i in range(len(seller)):
        price = amount[i] * 100
        idx = dic[seller[i]]
        while price > 0:
            if referral[idx] == "-":
                result[idx] += (price-price//10)
                break
            elif referral[idx] != "-":
                result[idx] += (price-price//10)
                idx = dic[referral[idx]]
                price = price // 10
    return result
