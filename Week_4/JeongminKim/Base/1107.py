"""

    0 ~ 9 숫자
    + , - 가 있다.
    + 를 누르면 현재 보고 있는 채널에서 +1 채널로 이동
    - 를 누르면 현재 보고 있는 채널에서 -1 채널로 이동

    이동 하려고 하는 채널은 N
    N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야 하는 지 구함

    수빈이가 지금 보고 있는 채널은 100

"""

if __name__ == '__main__':
    N = int(input())
    M = int(input())  # 고장 난 버튼의 개수
    if M:
        disabled = set(input().split())
    else:
        disabled = set()

    cur_channel = 100

    min_count = abs(cur_channel - N)
    for k in range(1000001):
        for i in str(k):
            if i in disabled:
                break
        else:
            min_count = min(min_count, abs(k - N) + len(str(k)))

    print(min_count)
