"""

    입력 값: 검증 수 0 4 2 5 6

    출력 수: 각 숫자를 제곱한 수들의 합을 10으로 나눈 나머지


"""

serial = list(map(int, input().split()))
serial = list(map(lambda x:x*x, serial))
retval = sum(serial) % 10
print(retval)