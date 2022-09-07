def solution(board, moves):
    bucket = []
    result = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] > 0:
                bucket.append(board[i][m - 1])
                if len(bucket) >= 2:
                    if bucket[len(bucket) - 2] == bucket[len(bucket) - 1]:
                        bucket = bucket[:len(bucket) - 2]
                        result += 2
                board[i][m - 1] = 0
                break
    return result
