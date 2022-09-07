def solution(board, moves):
    answer = 0
    basket = []
    h = [0 for _ in range(len(board[0]))]
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] > 0:
                h[i] = j
                break
    for x in moves:
        x = x-1
        if h[x] < len(board):
            basket.append(board[h[x]][x])
            board[h[x]][x] = 0
            h[x] += 1
            if len(basket) > 1 and basket[-1]==basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer