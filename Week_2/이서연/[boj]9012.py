'''
괄호

- 문제 요약
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 '('와 ')'만으로 구성되어 있는 문자열.
그 중 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS).
한 쌍의 괄호 기호로 된 "()"문자열은 기본 VPS.
만일 x가 VPS라면, 이것을 하나의 괄호에 넣은 새로운 문자열 "(x)"도 VPS.
두 VPS x와 y를 접합시킨 새로운 문자열 xy도 VPS.

입력으로 주어진 괄호 문자열이 VPS인지 아닌지를 판단해서 그 결과를 YES와 NO로 나타내는 프로그램.

- 입력 조건
첫째 줄에는 테스트케이스의 개수 T가 주어짐.
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어짐.
하나의 괄호 문자열의 길이는 2 이상 50 이하

- 출력 조건
올바른 괄호문자열(VPS)이면 "YES", 아니면 "NO"를 한 줄에 하나씩 출력
'''
t = int(input())

for _ in range(t):
    ps = input()
    left = ps.count('(')
    right = ps.count(')')
    
    if left != right:
        print('NO')
    
    else: # 왼쪽 괄호와 오른쪽 괄호 개수가 같으면
        for i in ps:
            if i == '(':
                left -= 1
            elif i == ')':
                right -= 1
            
            if left > right: # 남아있는 오른쪽 괄호 수가 더 많아야 함
                print('NO')
                break
        if left == 0 and right == 0:
            print('YES')
