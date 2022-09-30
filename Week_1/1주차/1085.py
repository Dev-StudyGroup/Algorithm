#입력
x, y, w, h = map(int, input().split())
#출력
result=min((w-x), x, (h-y), y)
print(result)
