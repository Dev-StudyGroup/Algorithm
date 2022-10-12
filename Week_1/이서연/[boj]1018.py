'''
체스판 다시 칠하기

- 문제 요약
검은색, 흰색으로 칠해져 있는 MN개의 단위 정사각형으로 나누어져 있는 MxN 크기의 보드를 잘라서 8*8크기의 체스판으로 만들려고 한다.
체스판은 검,흰 번갈아서 칠해져 있어야 한다. 체스판을 칠하는 경우는 2가지(맨 왼쪽 위 칸이 흰색인 경우, 검은색인 경우)
8*8 크기는 아무데서나 골라도 된다. 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램

- 입력 조건
첫째 줄에 N과 M이 주어짐. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수.
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어짐(B는 검은색, W는 흰색)

- 출력 조건
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값 출력
'''
n,m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))

min_count = 64

# 시작 위치 선택
for i in range(n-7):
    for j in range(m-7):
        # 시작 위치 board[i][j]
        count_a = 0 # 인덱스 합이 짝수인 칸을 B로 할 때 다시 칠해야 하는 개수
        count_b = 0 # 인덱스 합이 짝수인 칸을 W로 할 때 다시 칠해야 하는 개수
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0: 
                    if board[x][y] != 'B':
                        count_a += 1
                    if board[x][y] != 'W':
                        count_b += 1
                if (x + y) % 2 == 1:
                    if board[x][y] != 'W':
                        count_a += 1
                    if board[x][y] != 'B':
                        count_b += 1
        if (count_a < min_count):
            min_count = count_a
        if (count_b< min_count):
            min_count = count_b
print(min_count)

# count_a와 count_b의 합이 64가 되므로 하나만 구해서 작은 값을 택할 수 있음