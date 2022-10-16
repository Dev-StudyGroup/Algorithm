from collections import defaultdict
N = int(input())
dic = defaultdict(int)
for i in range(26):
    dic[chr(97+i)] = i+1
s = input()
res = 0
for i in range(len(s)):
    res += (dic[s[i]]*pow(31,i))
print(res%1234567891)