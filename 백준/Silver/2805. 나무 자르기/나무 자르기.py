n, m = map(int ,input().split())
lst = [i for i in map(int ,input().split())]

start = 0
end = max(lst)

while start <= end:
    mid = (start+end) // 2
    sum = 0
    for i in lst:
        if i > mid:
            sum += i-mid

    if sum < m:
        end = mid -1
    else:
        start = mid + 1
print(end)