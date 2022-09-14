notes = list(map(int, input().split()))
a,d=0,0
for i in range(len(notes)-1):
    if notes[i]<notes[i+1]:
        a+=1
    elif notes[i]>notes[i+1]:
        d+=1

if a == len(notes)-1:
    print("ascending")
elif d == len(notes)-1:
    print("descending")
else:
    print("mixed")