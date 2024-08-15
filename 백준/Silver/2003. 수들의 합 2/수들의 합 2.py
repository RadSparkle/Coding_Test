data, target = map(int, input().split())

list = list(map(int,input().split()))

interval_sum = 0
end = 0
count = 0
for start in range(data):
    while interval_sum < target and end < data:
        interval_sum += list[end]
        end+=1
    if interval_sum == target:
        count += 1
    interval_sum -= list[start]

print(count)