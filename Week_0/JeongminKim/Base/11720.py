cnt = int(input())
numbers = input()
retval = 0
for i in range(0, cnt):
    retval += int(numbers[i])

print(retval)