"""
    각 유저는 한번에 한명의 유저를 신고 가능
    신고 횟수는 제한 X
    서로 다른 유저를 계속해서 신고 가능
    한 유저를 여러번 신고 가능, 동일한 유저에 대한 신고횟수는 1회로 처리

    k번 이상 신고된 유저는 게시판 이용이 정지, 정지 사실은 메일로 발송
    모든 내용을 취합하여 마지막에 정지시키며 , 정지 메일을 발송
"""


def solution(id_list, report, k):
    answer = []

    report_list = dict()
    for user in id_list:
        report_list[user] = []
    for i in range(0, len(report)):
        user = report[i].split(" ")[0]
        reported_user = report[i].split(" ")[1]
        if user not in report_list[reported_user]:
            report_list[reported_user].append(user)
    stopped_id = []
    for reported_user in report_list.keys():
        if len(report_list[reported_user]) >= k:
            stopped_id.append(reported_user)
    result_mail = [0] * len(id_list)

    for stopped_user in stopped_id:
        for user in report_list[stopped_user]:
            result_mail[id_list.index(user)] += 1

    answer = result_mail
    return answer