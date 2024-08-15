import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

step = M
window = sum(numbers[:step])
answer = window

for i in range(step, N):
    window += numbers[i] - numbers[i - step]
    answer = max(answer, window)
print(answer)