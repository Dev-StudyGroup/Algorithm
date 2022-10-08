from collections import Counter
N = int(input())
numbers = []

def find_avg(numbers):
    avg = sum(numbers) / len(numbers)
    return round(avg)

def find_mid(numbers):
    return numbers[len(numbers) // 2]

def find_mode(numbers):
    commons = Counter(numbers).most_common()
    if len(numbers) > 1:
        if commons[0][1] == commons[1][1]:
            return commons[1][0]
        else:
            return commons[0][0]
    else:
        return commons[0][0]

def find_range(numbers):
    Min = min(numbers)
    Max = max(numbers)
    return Max - Min

for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
print(find_avg(numbers))
print(find_mid(numbers))
print(find_mode(numbers))
print(find_range(numbers))
