x, y, w, h = map(int, input().split())

xmin = min(x, w-x)
ymin = min(y, h-y)
print(min(xmin, ymin))