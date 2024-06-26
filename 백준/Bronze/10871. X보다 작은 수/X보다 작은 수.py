N, X = map(int, input().split())

A = list(map(int, input().split(' ')))

result = list()
for i in A:
    if i < X:
        result.append(i)

for i in result:
    print(i, end=' ')
