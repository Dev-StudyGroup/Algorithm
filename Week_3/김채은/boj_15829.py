from typing import Final

r: Final = 31
m: Final = 1234567891

l = int(input())
s = input()

answer = 0

for i in range(l):
    answer += (ord(s[i]) - 96) * (r ** i)

print(answer % m)

print(31**50)