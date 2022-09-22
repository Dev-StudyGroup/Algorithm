a, b = input().split()
a = int(a[::-1]) # 문자열 전체를 반대로
b = int(b[::-1])
if a > b:
    print(a)
else:
    print(b)