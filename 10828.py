'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys

input=sys.stdin.readline

class Stack:
    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, num):
        self.list.append(num)
        self.len += 1

    def pop(self):
        if self.size() == 0:
            return -1
        pop_result = self.list[self.len - 1]
        del self.list[self.len - 1]
        self.len -= 1
        return pop_result

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0

    def top(self):
        return self.list[-1] if self.size() != 0 else -1


num = int(input())
stack = Stack()

for i in range(num):
    input_split = input().split()

    op = input_split[0]

    if op == "push":
        stack.push(input_split[1])
    elif op == "pop":
        print(stack.pop())
    elif op == "size":
        print(stack.size())
    elif op == "empty":
        print(stack.empty())
    elif op == "top":
        print(stack.top())