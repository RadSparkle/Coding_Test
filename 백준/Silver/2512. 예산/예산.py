n = int(input())
budget = [i for i in map(int, input().split())]
target = int(input())

start, end = 1, max(budget)
result = 0
while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in budget:
        if i > mid:
            total+=mid
        else:
            total+= i

    if total <= target:
        start = mid+1
        result = mid
    else:
        end = mid-1
print(result)