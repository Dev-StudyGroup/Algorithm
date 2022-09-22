"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 신고 결과 받기
description : 파싱
"""

from typing import Final
from collections import defaultdict


def solution(idList, reportList, k):
    INIT_NUMBER: Final = 0
    ADD_NUMBER: Final = 1

    answer = []
    countReportUser = defaultdict(int)
    reportUserList = defaultdict(list)
    setReportList = list(set(reportList))

    for report in setReportList:
        fromUser, toUser = report.split()
        countReportUser[toUser] += ADD_NUMBER
        reportUserList[fromUser].append(toUser)

    for userId in idList:
        count = INIT_NUMBER

        for toUser in reportUserList[userId]:
            if countReportUser[toUser] >= k:
                count += ADD_NUMBER

        answer.append(count)

    return answer


if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
