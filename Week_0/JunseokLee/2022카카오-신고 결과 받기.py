from collections import defaultdict

dic = defaultdict(int)
dic1 = defaultdict(int)


def solution(id_list, report, k):
    global dic, dic1
    result = []
    report = set(report)  # 중복 제거
    report = list(report)  #
    for i in range(len(id_list)):  # 필요 없는 코드 - 이유? defaultdict(int)쓰면 자동으로 0으로 초기화
        dic[id_list[i]] = 0
        dic1[id_list[i]] = 0
    for i in range(len(report)):
        reporting, reported = report[i].split(' ')
        dic[reported] += 1

    banned = set()
    for i in range(len(id_list)):
        if dic[id_list[i]] >= k:
            banned.add(id_list[i])

    for i in range(len(report)):
        reporting, reported = report[i].split(' ')
        if reported in banned:
            dic1[reporting] += 1
    for i in range(len(id_list)):
        result.append(dic1[id_list[i]])

    return result
