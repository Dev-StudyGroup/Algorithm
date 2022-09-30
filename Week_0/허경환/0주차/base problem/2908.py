#입력
a, b = input().split()

ls_a=list(a)
ls_b=list(b)

str_a=""
str_b=""

for i in range(2,-1,-1):
    str_a+=ls_a[i]
    str_b+=ls_b[i]

#출력
result_a=int(str_a)
result_b=int(str_b)

if result_a>result_b:
    print(result_a)
else:
    print(result_b)
