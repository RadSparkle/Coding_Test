from collections import deque
import sys
stack_left = []
stack_right = deque()
word_list = []
results = []

# 입력 처리
for _ in range(int(sys.stdin.readline().rstrip())):
    word_list.append(sys.stdin.readline().rstrip())

# 입력 처리 및 결과 저장
for k in word_list:
    for i in k:
        if i == '<':
            if stack_left:
                stack_right.appendleft(stack_left.pop())
        elif i == '>':
            if stack_right:
                stack_left.append(stack_right.popleft())
        elif i == '-':
            if stack_left:
                stack_left.pop()
        else:
            stack_left.append(i)
    # 결과 저장
    results.append(''.join(stack_left + list(stack_right)))
    # 스택 초기화
    stack_left = []
    stack_right = deque()

# 한 번에 출력
sys.stdout.write('\n'.join(results) + '\n')
