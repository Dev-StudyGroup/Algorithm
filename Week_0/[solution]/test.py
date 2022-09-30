'''
맨 왼쪽 위 칸이 흰색
맨 왼쪽 위 칸이 검은색

'''

N, M = map(int, input().split())

board = []
wb_board = ["WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW"]

bw_board = ["BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB", ]

for _ in range(N):
    temp = input()
    board.append(temp)

answer = int(1e9)

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        count1 = 0  # 흑백으로 시작 몇개 고쳐야되는지
        count2 = 0  # 백흑 ~~

        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if board[r][c] != wb_board[r - i][c - j]:
                    count1 += 1
                if board[r][c] != bw_board[r - i][c - j]:
                    count2 += 1
        answer = min(answer, count1, count2)
print(answer)
