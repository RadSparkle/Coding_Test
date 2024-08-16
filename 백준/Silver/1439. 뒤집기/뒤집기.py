s = [i for i in str(input())]
stack = []
for i in s:
    if len(stack) > 0 and stack[-1] == i:
        continue
    else:
        stack.append(i)
print(min(stack.count('0'), stack.count('1')))