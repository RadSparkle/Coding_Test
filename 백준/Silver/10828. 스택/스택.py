
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return 1 if len(self.items) == 0 else 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return -1
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return -1

    def size(self):
        return len(self.items)

stack = Stack()

N = int(input())
result = []
for _ in range(N):
    a  = list(map(str, input().split(' ')))

    if 'push' in a:
        stack.push(a[1])
    elif 'top' in a:
        result.append(stack.top())
    elif 'size' in a:
        result.append(stack.size())
    elif 'empty' in a:
        result.append(stack.is_empty())
    elif 'pop' in a:
        result.append(stack.pop())

for i in result:
    print(i)