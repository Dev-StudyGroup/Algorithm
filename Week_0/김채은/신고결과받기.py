# [Programmers] 92334 신고 결과 받기
# Time Taken: 27m

from collections import defaultdict

def solution(id_list, reports, k):
    answer = []

    report_dict = defaultdict(list)
    
    for report in reports:
        reporter, reported = report.split()

        if reporter not in report_dict[reported]:
            report_dict[reported].append(reporter)

    mail = defaultdict(int)

    for item in report_dict.items():
        reported, reporters = item

        if len(reporters) >= k:
            for reporter in reporters:
                mail[reporter] += 1

    for id in id_list:
        answer.append(mail[id])

    return answer

