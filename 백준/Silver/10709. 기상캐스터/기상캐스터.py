h, w = map(int, input().split())
city = [[-1 for _ in range(w)] for _ in range(h)]

for i in range(h):
    cloud = list(map(str, input()))

    for idx, value in enumerate(cloud):
        if value == 'c':
            city[i][idx] = 0
            tmp = 0
            for k in range(idx, w):
                city[i][k] = tmp
                tmp+=1
for i in city:
    print(*i)