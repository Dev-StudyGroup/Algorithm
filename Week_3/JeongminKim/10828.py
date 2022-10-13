"""

    스택을 구현

    명령은 총 다섯가지이다.

    push X: 정수 X 스택에 넣는 연산이다.
    pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 없는 경우 -1를 출력한다.
    size: 스택에 들어있는 정수의 개수를 출력한다.
    empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    top: 스택이 가장 위에 있는 정수를 출력한다. 스택에 들어있는 정수가 없는 경우 -1를 출력한다.

"""


class Stack:

    def __init__(self):
        self.stack = []
        self.__top = None
        self.__size = 0

    def push(self, value):
        self.stack.append(value)
        self.__top = self.stack[-1]
        self.__size += 1

    def pop(self):
        if self.stack:
            ret = self.stack.pop(-1)
            self.__size -= 1
            if self.stack:
                self.__top = self.stack[-1]
            else:
                self.__top = None
            return ret
        else:
            self.__top = None
            return -1

    def size(self):
        return self.__size

    def empty(self):
        if self.__size < 1:
            return 1
        else:
            return 0

    def top(self):
        if not self.__top:
            return -1
        return self.__top


if __name__ == '__main__':
    import sys
    N = int(input())
    s = Stack()
    for _ in range(N):
        temp = sys.stdin.readline().split()
        if len(temp) == 2:
            method = temp[0]
            value = temp[1]
            value = int(value)
        if len(temp) == 1:
            method = temp[0]

        if method == 'push':
            s.push(value)

        if method == 'top':
            print(s.top())

        if method == 'size':
            print(s.size())

        if method == 'empty':
            print(s.empty())

        if method == 'pop':
            print(s.pop())
