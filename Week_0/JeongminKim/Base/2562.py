
maxnum = -1
maxnum_index = 0
numlist = []


for i in range(0, 9):
    numlist.append(int(input()))

for i in range(0, 9):
    if maxnum < numlist[i]:
        maxnum = numlist[i]
        maxnum_index = i+1

print(maxnum, maxnum_index, sep='\n')