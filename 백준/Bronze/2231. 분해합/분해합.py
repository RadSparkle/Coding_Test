n = int(input())

for i in range(1, n+1):
    test = list(map(int, str(i)))
    if i + sum(test) == n:
        print(i)
        break

    if i == n:
        print(0)
