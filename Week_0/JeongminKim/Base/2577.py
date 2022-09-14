"""

    세 개의 자연수 A, B, C가 주어지고,

    입력값: 세 개의 자연수가 주어짐

    출력값: 세 개의 자연수를 곱한 결과 각각의 숫자가 몇번 쓰였는지

    3.8 버전 부터 math.prod 제공

"""
import math
num = []
cnt = [0] * 10

for _ in range(3):
    num.append(int(input()))
multi = str(math.prod(num))

for n in multi:
    cnt[int(n)] += 1

for i in range(0, 10):
    print(cnt[i])