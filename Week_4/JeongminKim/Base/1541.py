"""

    양수와 +, - 그리고 괄호를 가지고 식을 만들었고,

    괄호를 모두 지웠다.

    괄호를 적절히 쳐서 최소로 만들라 할때 최소값은?

"""
arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
