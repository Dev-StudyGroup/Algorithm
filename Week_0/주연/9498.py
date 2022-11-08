Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
score=int(input())
    
if score >= 90:
    print('A')
elif score <= 89 and score >= 80:
    print('B')
elif score <= 79 and score >= 70:
    print('C')
elif score <= 69 and score >= 60:
    print('D')
else:
    print('F')