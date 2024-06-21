N, M = map(int, input().split())

left = 1
right = M
result = 0
j = int(input())

for _ in range(j):
    position = int(input())

    if left <= position and right >= position:
        continue
    elif left > position:
        result += (left - position)
        right -= left - position
        left = position
    elif right < position:
        result += (position - right)
        left += position - right
        right = position
print(result)