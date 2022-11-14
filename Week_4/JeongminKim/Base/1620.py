"""

    도감엔 포켓몬 입력 순서대로

    포켓몬 : 포켓몬 입력 순서 번호

"""


def print_result(result):
    return '\n'.join(result)


if __name__ == '__main__':
    from collections import defaultdict

    N, M = map(int, input().split())
    book = defaultdict()
    for i in range(1, N + 1):
        pokemon = input()
        book[pokemon] = str(i)
        book[str(i)] = pokemon
    result = []
    for _ in range(M):
        question = input()
        result.append(book[question])

    print(print_result(result))
