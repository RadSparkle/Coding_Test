import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    else:
        if len(stack) > 0:
            print(int(stack[-1]))
        else:
            print(-1)

