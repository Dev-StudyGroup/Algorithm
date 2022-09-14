def solution(numbers, hand):
    answer = ''
    left, right = [3, 0], [3, 2]
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            left = [n // 3, 0]
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            right = [n // 3 - 1, 2]
        else:
            if n == 0:
                n = 11
            ldist = abs(n // 3 - left[0]) + abs(1 - left[1])
            rdist = abs(n // 3 - right[0]) + abs(1 - right[1])
            if ldist < rdist:
                answer += 'L'
                left = [n // 3, 1]
            elif ldist > rdist:
                answer += 'R'
                right = [n // 3, 1]
            else:  # 두 손과 중앙에 위치한 키패드 거리가 같을 때
                if hand == "left":
                    answer += 'L'
                    left = [n // 3, 1]
                elif hand == "right":
                    answer += 'R'
                    right = [n // 3, 1]
    return answer
