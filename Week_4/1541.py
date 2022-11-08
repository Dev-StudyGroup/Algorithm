"""
1541: 잃어버린 괄호
* 그리디 알고리즘 문제

양수, +, -, 괄호를 사용한 식을 만든 후 괄호를 제거한다.
그리고 나서 괄호를 적절히 쳐 이 식의 값을 최소로 만들려고 한다.
"""

expression = input().split("-")
result = 0

for i in expression[0].split("+"):
    result += int(i)
for i in expression[1:]:
    for j in i.split("+"):
        result -= int(j)

print(result)
