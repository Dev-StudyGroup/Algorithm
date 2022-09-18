"""
    처음 상태
        + 왼손: * 키패드에
        + 오른손: # 키패드에서
    시작.

    엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있음
    왼쪽열 3개 1, 4, 7은 왼손
    오른쪽열 3개 3, 6, 9는 오른손
    가운데 열 4개 2, 5, 8, 0 두 엄지 손가락의 현재 키패드의 위치에서 더 가까운 엄지 손가락 이용
    두 엄지 손가락의 거리가 같다면,
        + 오른손잡이는 오른손
        + 왼손잡이는 왼손


"""

def distance(key, keyloc, keypad, thumb):

    kloc = keyloc[key]
    tloc = keyloc[thumb]

    if kloc != tloc:
        return abs(keypad[kloc].index(key) - keypad[tloc].index(thumb)) + 1
    else:
        return abs(keypad[kloc].index(key) - keypad[tloc].index(thumb))

def solution(numbers, hand):
    answer = ''
    keyloc = dict()
    keypad = {'left':[1,4,7,"*"], 'right':[3,6,9,'#'], 'mid':[2,5,8,0]}
    for k, v in keypad.items():
        for i in v:
            keyloc[i] = k
    lthumb = '*'
    rthumb = '#'
    for key in numbers:
        if keyloc[key] == 'left':
            lthumb = key
            answer += 'L'
        if keyloc[key] == 'right':
            rthumb = key
            answer += 'R'
        if keyloc[key] == 'mid':
            ld = distance(key, keyloc, keypad, lthumb)
            rd = distance(key, keyloc, keypad, rthumb)
            if hand == 'left':
                if ld > rd:
                    rthumb = key
                    answer += 'R'
                else:
                    lthumb = key
                    answer += 'L'

            if hand == 'right':
                if ld < rd:
                    lthumb = key
                    answer += 'L'
                else:
                    rthumb = key
                    answer += 'R'
    return answer


