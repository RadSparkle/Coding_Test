a, b, c = map(int, input().split())

t1, t2 = map(int, input().split())
t3, t4 = map(int, input().split())
t5, t6 = map(int, input().split())

time_line = [[] for _ in range(max(t1, t2, t3, t4, t5, t6) + 1)]

for i in range(t1+1, t2 + 1):
    time_line[i].append(1)

for i in range(t3+1, t4 + 1):
    time_line[i].append(1)

for i in range(t5+1, t6 + 1):
    time_line[i].append(1)

result = 0

for i in time_line:
    if len(i) == 1:
        result += len(i) * a
    if len(i) == 2:
        result += len(i) * b
    if len(i) == 3:
        result += len(i) * c
print(result)