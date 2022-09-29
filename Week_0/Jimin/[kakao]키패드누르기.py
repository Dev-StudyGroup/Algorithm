'''
'키패드 누르기'
'''
def solution(numbers, hand):
    board = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
    answer = ""
    nowR = [3, 2]
    nowL = [3, 0]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            nowL = [i//3, 0]
            answer += "L"
        elif i == 3 or i == 6 or i == 9:
            nowR = [i//3-1, 2]
            answer += "R"
        else:
            if i == 0:
                x = 3
            else:
                x = i//3
            y = 1
            distanceL = abs(nowL[0]-x) + abs(nowL[1]-y)
            distanceR = abs(nowR[0]-x) + abs(nowR[1]-y)

            if distanceL < distanceR:
                answer += "L"
                nowL = [x, y]
            elif distanceL > distanceR:
                answer += "R"
                nowR = [x, y]
            else:
                if hand == "right":
                    answer += "R"
                    nowR = [x, y]
                else:
                    answer += "L"
                    nowL = [x, y]

    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))