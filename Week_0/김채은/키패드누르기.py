# [Programmers] 67256 키패드 누르기
# Time Taken: 31m

def solution(numbers, hand):
    answer = ''

    hand = 'R' if hand == "right" else 'L'    
    left_current, right_current = '*', '#'

    keypad = dict()
    key = [str(i) for i in range(1, 10)] + ['*', '0', '#']
    for i in range(12):
        keypad[key[i]] = (i//3, i%3)

    def getDistance(key1, key2):
        key1_y, key1_x = keypad[key1]
        key2_y, key2_x = keypad[key2]

        return abs(key1_y - key2_y) + abs(key1_x - key2_x)

    def getNear(key):
        left_dist = getDistance(left_current, key)
        right_dist = getDistance(right_current, key)
        if left_dist > right_dist:
            return 'R'
        elif left_dist < right_dist:
            return 'L'
        else:
            return hand

    for number in numbers:
        remain = number % 3
        near = ''

        if number == 0 or remain == 2:
            near = getNear(str(number))
            answer += near

        elif remain == 1:
            near = 'L'
            answer += 'L'
        else:
            near = 'R'
            answer += 'R'

        if near == 'L':
            left_current = str(number)   
        else:
            right_current = str(number)
            
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")