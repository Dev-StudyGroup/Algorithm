'''
분해합

- 문제 요약
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
ex) 245의 분해합은 245 + 2 + 4 + 5 = 256 (245는 256의 생성자)
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램

- 입력 조건
첫째 줄에 자연수 N(1<= N <= 1,000,000)이 주어짐

- 출력 조건
첫째 줄에 답을 출력. 생성자가 없는 경우에는 0 출력.
'''
n = int(input())
curr = 0
result = 0
while curr < n:
    curr += 1
    total = curr + sum(list(map(int, str(curr))))

    if total == n:
        result = curr
        break

print(result)
