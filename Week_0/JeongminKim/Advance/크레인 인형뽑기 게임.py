def make_new_board(board):
    new_board = dict()
    for i in range(len(board)-1, -1, -1):
        for j in range(0, len(board)):
                if (j+1) not in new_board.keys():
                    if board[i][j] == 0:
                        new_board[j+1] = []
                    else:
                        new_board[j+1] = [board[i][j]]
                else:
                    if board[i][j] != 0:
                        new_board[j+1].append(board[i][j])
    return new_board


def getitem(new_board, moves):
    cnt = len(new_board[moves])
    if cnt > 0:
        return new_board[moves].pop(-1)


def solution(board, moves):
    answer = 0

    new_board = make_new_board(board)
    bucket = []

    for move in moves:
        item = getitem(new_board, move)
        if item:
            if len(bucket) > 0 and bucket[-1] == item:
                bucket.pop(-1)
                answer += 2
            else:
                bucket.append(item)
    print(bucket, answer)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])