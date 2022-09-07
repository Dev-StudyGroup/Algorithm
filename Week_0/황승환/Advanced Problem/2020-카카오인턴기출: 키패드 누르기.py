def solution(numbers, hand):
    answer = []
    left, right = (3, 0), (3, 2)
    keypad = [(3, 1)]
    for i in range(3):
        for j in range(3):
            keypad.append((i, j))
    for number in numbers:
        if number in (1, 4, 7):
            answer.append('L')
            left = keypad[number]
        elif number in (3, 6, 9):
            answer.append('R')
            right = keypad[number]
        else:
            l_dist = abs(left[0]-keypad[number][0])+abs(left[1]-keypad[number][1])
            r_dist = abs(right[0]-keypad[number][0])+abs(right[1]-keypad[number][1])
            if l_dist < r_dist:
                answer.append('L')
                left = keypad[number]
            elif l_dist > r_dist:
                answer.append('R')
                right = keypad[number]
            else:
                if hand == 'left':
                    answer.append('L')
                    left = keypad[number]
                else:
                    answer.append('R')
                    right = keypad[number]
    return ''.join(answer)