def solution(numbers, hand):
    # numbers : 누를 번호
    # hand : 무슨 손잡이
    answer = ''
    hand = hand[0].upper()
    L = 10; R = 12; left = [1, 4, 7]; right = [3, 6, 9]
    for i in numbers:
        if i == 0: i = 11
        if i in left:
            answer += "L"
            L = i
        elif i in right:
            answer += "R"
            R = i
        else:
            if i % 3 == L % 3: Llen = abs(i // 3 - L // 3)
            else: Llen = abs(i // 3 - L // 3) + 1
            if i % 3 == R % 3: Rlen = abs(i // 3 - R // 3)
            else: Rlen = abs(i // 3 - (R // 3 - 1)) + 1

            if Llen == Rlen:
                answer += hand
                if hand == "L": L = i
                else: R = i
            elif Llen > Rlen:
                answer += "R"
                R = i
            else:
                L = i
                answer += "L"
    return answer