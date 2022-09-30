'''
상수

- 문제 요약
두 수가 주어졌을 때, 상수는 수를 거꾸로 읽음.
ex) 734와 893을 437과 398로
거꾸로 읽은 수 중 크기가 큰 수를 출력하는 프로그램(예시에서는 437)

- 입력 조건
첫째 줄에 두 수 A와 B가 주어짐.
두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않음

- 출력 조건
첫째 줄에 상수의 대답을 출력
'''
a, b = input().split()
reversed_a = int(a[::-1])
reversed_b = int(b[::-1])

# '문자열을 리스트로 -> 리스트 역순(list.reverse()) -> 문자열' 방법도 있음
# reversed() 함수는 인자로 리스트 뿐 아니라 튜플, 문자열 받을 수 있음. 반복자 반환함
# reversed_a = int(''.join(reversed(a)))

if (reversed_a > reversed_b):
    print(reversed_a)
else:
    print(reversed_b)