def solution(id_list, report, k):
    # id_list : 사용자의 ID
    # report : 각 이용자가 신고한 이용자의 ID가 담긴 문자열 배열
    # k : 정지 기준이 되는 신고 횟수
    answer = [0] * len(id_list)
    arr = [] # 1
    count = [0] * len(id_list)
    for i in range(len(id_list)):
        arr.append(set())
    # print(arr)
    for i in range(len(report)):
        a, b = report[i].split()
        for j in range(len(id_list)):
            if id_list[j] == a:
                arr[j].add(b)

    for i in range(len(arr)):
        for j in range(len(arr)):
            if id_list[i] in arr[j]:
                count[i] += 1

    for i in range(len(id_list)):
        if count[i] >= k:
            for j in range(len(arr)):
                if id_list[i] in arr[j]:
                    answer[j] += 1
    return answer