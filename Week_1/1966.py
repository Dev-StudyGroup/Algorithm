"""

    1. queue 가장 앞에 있는 문서의 중요도 확인
    2. 나머지 문서들 중에서 현재 문서보다 중요도가 높은 문서가 하나라도 있으면 큐 뒤에 재배치한다.

    첫번째 줄은 test_case 수
    N / M
    문서의 개수 / M번째 문서가 몇번째로 출력되었는지 출력
    두 번째 줄에는
    N개 문서의 중요도가 차례대로 주어짐

"""

def solution(priorities, location):
    answer = 0
    orders = [0] * len(priorities)
    cur_loc = 0
    job = []
    for i in range(0, len(priorities)):
        job.append((priorities[i],i))
    print_order = 1
    while len(job) > 0:
        cur_pri, cur_index = job.pop(0)
        if len(job) > 0:
            max_pri, max_index = job[job.index(max(job))]
        else:
            break
        if cur_pri < max_pri:
            # temp_job = job.pop(job.index(max(job)))
            job.append((cur_pri, cur_index))
            # cur_pri, cur_index = temp_job
            # orders[cur_index] = print_order
        else:
            orders[cur_index] = print_order
            print_order += 1

    orders[cur_index] = print_order
    answer = orders[location]
    return answer


t = int(input())
result = []
for _ in range(t):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))

    result.append(solution(ls, M))

for r in result:
    print(r)




