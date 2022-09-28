import sys
input = sys.stdin.readline

t = input().rstrip()
t = t.upper()
m = dict()
for i in t:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
t = []
for k, v in m.items():
    if v == max(m.values()):
        t.append(k)
if len(t) == 1:
    print(t[0])
else:
    print("?")
