'''
숫자 카드 2

- 문제 요약
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 구하는 프로그램

- 입력 조건
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N (1 <= N <= 500,000)이 주어진다.
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. (-10,000,000 이상 10,000,000 이하)
셋째 줄에는 M (1 <= M <= 500,000)이 주어진다.
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어 있다. (-10,000,000 이상 10,000,000 이하)

- 출력 조건
첫째 줄에 입력으로 주어진 M개의 수에 대해 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력
'''
n = int(input())
card = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

count_dict = {}

for i in card:
    if i not in count_dict:
        count_dict[i] = 1
    else:
        count_dict[i] += 1

for j in num:
    if j not in count_dict:
        print(0, end=' ')
    else:
        print(count_dict[j], end=' ')
