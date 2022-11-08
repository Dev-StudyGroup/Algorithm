N = int(input())
answer = 666
cnt = 0

while True:
    if '666' in str(answer):
        cnt += 1
    if cnt == N:
        print(answer)
        break
    answer += 1
