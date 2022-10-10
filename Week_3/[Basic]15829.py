n = int(input())
string = input()

result = 0
for i in range(n):
    str_num = ord(string[i]) - 96
    result += str_num * (31 ** i)

m = 1234567891
print(result % m)