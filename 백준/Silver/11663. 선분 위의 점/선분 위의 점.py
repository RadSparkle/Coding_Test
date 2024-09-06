import bisect

n, m = map(int, input().split())
point_list = [i for i in map(int, input().split())]

point_list.sort()
result = []
for _ in range(m):
    a, b = map(int, input().split())
    left_idx = bisect.bisect_left(point_list, a)
    right_idx = bisect.bisect_right(point_list, b)
    result.append(right_idx-left_idx)

for i in result:
    print(i)