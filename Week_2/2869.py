#입력
a, b, v = map(int, input().split())

#구현
if (v-a)%(a-b)==0:
    result=(v-a)//(a-b)+1
else:
    result=(v-a)//(a-b)+2
    
print(result)
