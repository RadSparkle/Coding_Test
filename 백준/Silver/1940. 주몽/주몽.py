N = int(input())
M = int(input())
list = list(map(int, input().split()))

list.sort()

start = 0
end = N - 1
count = 0

while start != end:
    if list[start] + list[end] == M:
        count += 1
        start += 1
    elif list[start] + list[end] > M:
        end -= 1
    elif list[start] + list[end] < M:
        start += 1

print(count)