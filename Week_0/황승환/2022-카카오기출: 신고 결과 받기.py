from collections import defaultdict
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    rep = defaultdict(list)
    reported = defaultdict(int)
    cnt = defaultdict(int)
    for i in range(len(report)):
        report[i] = list(map(str, report[i].split()))
        if report[i][1] not in rep[report[i][0]]:
            rep[report[i][0]].append(report[i][1])
            reported[report[i][1]] += 1
    for key, lst in rep.items():
        for name in lst:
            if reported[name] >= k:
                cnt[key] += 1
    for i in range(len(id_list)):
        answer[i] = cnt[id_list[i]]
    return answer