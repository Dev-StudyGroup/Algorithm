'''
크레인 인형뽑기 게임
'''
def solution(board, moves):
    answer = 0
    doll_list = []

    new_board = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[j].append(board[i][j])

    for i in moves:
        for j in range(len(new_board[i-1])):
            temp = new_board[i-1][j]
            if temp != 0:
                if len(doll_list) == 0:
                    doll_list.append(temp)
                elif temp == doll_list[-1]:
                    doll_list.pop()
                    answer += 2
                else:
                    doll_list.append(temp)
                new_board[i-1][j] = 0
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))