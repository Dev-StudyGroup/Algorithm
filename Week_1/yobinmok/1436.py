# https://www.acmicpc.net/problem/1436
n = int(input())

i = 666
while True:
    num = str(i)
    if "666" in num:
        count += 1
        if count == n:
            print(i)
    i += 1





































# num = 666; count = 0

# while True:
#     if "666" in str(num):
#         count += 1
#     if count == n:
#         print(num)
#         break
#     num += 1