L = int(input())
str = input().rstrip()
answer = 0

for i in range(len(str)):
    answer += (ord(str[i]) - 96) * (31 ** i)

print(answer % 1234567891)
