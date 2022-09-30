n, m = map(int, input().split()) # n 행, m 열

chess = []
count = []

for i in range(n):
    chess.append(input())

for i in range(n-7):
    for j in range(m-7):
        countB = 0; countW = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0: # 시작점과 색이 같아야 함
                    if chess[k][l] != "W":
                        countW += 1
                    else:
                        countB += 1
                else:
                    if chess[k][l] != "W":
                        countB += 1
                    else:
                        countW += 1
        count.append(min(countB, countW))

print(min(count))

































# if chess[0][0] == "W":
#     for i in range(n):
#         for j in range(m):
#             if i % 2 == 0:
#                 if j % 2 == 0 and chess[i][j] != "W":
#                     count += 1
#                 elif j % 2 == 1 and chess[i][j] != "B":
#                     count += 1
#             else:
#                 if j % 2 == 0 and chess[i][j] != "B":
#                     count += 1
#                 elif j % 2 == 1 and chess[i][j] != "W":
#                     count += 1
#     chess[0][0] = "B"
# else:
#     for i in range(n):
#         for j in range(m):
#             if i % 2 == 0:
#                 if j % 2 == 0 and chess[i][j] != "B":
#                     count += 1
#                 elif j % 2 == 1 and chess[i][j] != "W":
#                     count += 1
#             else:
#                 if j % 2 == 0 and chess[i][j] != "W":
#                     count += 1
#                 elif j % 2 == 1 and chess[i][j] != "B":
#                     count += 1
#     chess[0][0] = "W"



# if count > count2:
#     print(count2)
# else:
#     print(count)
"""
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
"""