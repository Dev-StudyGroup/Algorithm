Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
tone=input()
if tone == '1 2 3 4 5 6 7 8':
    print('ascending')
elif tone == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')