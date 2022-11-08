"""
1620: 나는야 포켓몬 마스터 이다솜
* index 함수의 시간복잡도는(O(n))로 인한 시간초과 문제 발생
  해쉬 자료구조의 경우 시간복잡도가 O(1)이다 -> dict 사용!
"""
import sys
# n: 포켓몬의 개수, m: 맞춰야 하는 문제의 개수
n, m = map(int, input().split())
poketmon_num = {} # 1 = pikachu
poketmon_name = {} # pikachu = 1

for i in range(n):
    name = sys.stdin.readline().strip()
    poketmon_num[i] = name
    poketmon_name[name] = i

for _ in range(m):
    problem = sys.stdin.readline().strip()
    if problem.isdigit(): # 문제가 숫자이면
        print(poketmon_num[int(problem)-1])
    else: # 문제가 문자이면
        print(poketmon_name[problem] + 1)
    