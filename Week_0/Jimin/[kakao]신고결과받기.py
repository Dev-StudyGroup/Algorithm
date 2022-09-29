'''
'신고 결과 받기'
'''
def solution(id_list, report, k):
    report_member = {}
    report_cnt = {}
    answer = {}
    for i in id_list:
        answer[i] = 0

    for i in report:
        a, b = i.split()
        if b in report_member:
            if a in report_member[b]:
                continue
            else:
                report_member[b].append(a)
                if b in report_cnt:
                    report_cnt[b] += 1
                else:
                    report_cnt[b] = 1
        else:
            report_member[b] = [a]
            if b in report_cnt:
                report_cnt[b] += 1
            else:
                report_cnt[b] = 1

    for i in report_cnt:
        if report_cnt[i] >= k:
            for j in report_member[i]:
                answer[j] += 1
    return(list(answer.values()))

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))