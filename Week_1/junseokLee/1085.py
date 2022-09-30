x,y,w,h=map(int, input().split())
result = 1000
result = min(x,y)
result = min(result, min(w-x,h-y))
print(result)