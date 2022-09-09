# [Programmers] 64061 크레인 인형뽑기 게임
# Time Taken: 19m

def solution(board, moves):
    global answer
    answer = 0

    rboard = list(map(list, zip(*board)))

    bucket = []

    def putBucket(doll):
        global answer
        if not bucket or bucket[-1] != doll:
            bucket.append(doll)
        else:
            bucket.pop()
            answer += 2

    for move in moves:
        for idx, doll in enumerate(rboard[move-1]):
            if doll == 0:
                continue
            putBucket(doll)
            rboard[move-1][idx] = 0
            break
        
    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])