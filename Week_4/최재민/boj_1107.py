n = int(input())
m = int(input())
broken = []
if m != 0:  # 고장난게 없을수도??
  broken = list(input())

ans = abs(100 - n)

for channel in range(1000001):
  channel = str(channel)
  for j in range(len(channel)):
    if channel[j] in broken:
      break
    elif j == len(channel) - 1:
      ans = min(ans, abs(int(channel)-n) + len(channel))

print(ans)