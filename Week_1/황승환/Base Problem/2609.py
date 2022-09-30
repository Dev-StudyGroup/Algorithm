# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
#
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
a, b = map(int, input().split())
gcd, lcm = 0, 0
for i in range(min(a, b), 0, -1):
    if a%i == 0 and b%i == 0:
        gcd = i
        break
for i in range(max(a, b), (a*b)+1):
    if i%a == 0 and i%b == 0:
        lcm = i
        break
print(gcd)
print(lcm)
