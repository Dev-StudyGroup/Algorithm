"""
15829: Hashing

알파벳별로 숫자가 정해져 있음. 
따라서 입력받은 문자열을 숫자로 표현할 수 있다.
각 숫자들에 r^i를 곱한 값의 합을 해쉬값으로 정한다.

* a의 아스키 코드 값: 97
"""
L = int(input())
string = input(); sum = 0

for i in range(len(string)):
    sum += (ord(string[i])-96) * (31 ** i)

h = sum % 1234567891
print(h)
