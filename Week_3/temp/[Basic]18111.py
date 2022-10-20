import bisect

n, m, b = map(int, input().split())
num = n * m
ground = []
for _ in range(n):
    ground += list(map(int, input().split()))
    

def removeBlock(standard):
    time, inventory = 0, 0
    idx = bisect.bisect_right(ground, standard)

    for i in range(idx, num):
        number = ground[i] - standard
        time += 2 * number
        inventory += number

    return inventory, time


def addBlock(standard):
    time, inventory = 0, 0
    idx = bisect.bisect_left(ground, standard)

    for i in range(idx):
        number = standard - ground[i]
        time += number
        inventory -= number

    return inventory, time

ground.sort()
max_val, min_val = ground[-1], ground[0]
result = (int(1e9), 0)

for val in range(max_val, min_val-1, -1):
    remove_inventory, remove_time = removeBlock(val)
    add_inventory, add_time = addBlock(val)
    
    if b + remove_inventory + add_inventory >= 0:
        result = min(result, (remove_time + add_time, -val))

print(result[0], -result[1])