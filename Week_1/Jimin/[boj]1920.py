'''
'수 찾기'
'''
N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

N_list = sorted(N_list)

for i in M_list:
    start = 0
    end = N-1
    answer = 0
    while start <= end:
        mid = (start+end) // 2
        if N_list[mid] < i:
            start = mid + 1
        elif N_list[mid] > i:
            end = mid - 1
        else:
            answer = 1
            break

    print(answer)