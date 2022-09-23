# ver 1 : 길이는 짧지만 시간은 긺
n = int(input())
nums = []; s = 0
for i in range(n):
    s = i; i = str(i)
    for j in range(len(i)):
        s += int(i[j]) # 분해합 구함
    if s == n:
        answer = i
        break;
    else:
        answer = 0
print(answer)

# ver 2 : 길이는 길지만 시간은 짧음 ... 근데 차이 개적음
n = int(input())
nums = []; s = 0
for i in range(n):
    s = i
    i = str(i)
    for j in range(len(i)):
        s += int(i[j]) # 분해합 구함
    if s == n:
        nums.append(i)
if len(nums) == 0:
    print("0")
else:
    print(nums)


# 해결 잘했다
# N = int(input())
# for gen in range(1, N):
#     gen_nums = list(map(int, list(str(gen))))
#     if gen + sum(gen_nums) == N:
#         break
#     else:
#         gen = 0
# print(gen)