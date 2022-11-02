'''
'다단계 칫솔 판매'
'''
def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    index_dic = {}
    for i in range(len(enroll)):
        index_dic[enroll[i]] = i

    for i in range(len(referral)):
        if referral[i] in index_dic:
            referral[i] = index_dic[referral[i]]

    for i in range(len(seller)):
        idx = index_dic[seller[i]]
        money = amount[i] * 100

        while True:
            temp = money // 10
            if temp < 1:
                answer[idx] += money
                break
            if referral[idx] == '-':
                answer[idx] += money - temp
                break
            else:
                answer[idx] += money - temp
            money = temp
            idx = referral[idx]

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
