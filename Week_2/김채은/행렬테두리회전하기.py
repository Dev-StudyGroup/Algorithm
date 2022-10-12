def solution(rows, columns, queries):
    board = [i for i in range((rows*columns)+1)]
    answer = []

    for q in queries:
        x1, y1, x2, y2 = map(int, q)
        move_count = [y2 - y1, x2 - x1, y2 - y1, x2 - x1 - 1]
        move = [1, columns, -1, -columns]
        change = [(x1-1) * columns + y1]

        i=0
        for mc, m in zip(move_count, move):
            for i in range(mc):
                change.append(change[-1] + m)

        _min = 10001
        temp = board[change[-1]]
        
        for i in range(len(change)-1, 0, -1):
            board[change[i]] = board[change[i-1]]
            _min = min(_min, board[change[i]])

        board[change[0]] = temp

        _min = min(_min, board[change[0]])
        answer.append(_min)
        
    return answer