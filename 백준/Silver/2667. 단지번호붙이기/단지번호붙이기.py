from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    map[x][y]=0
    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N and map[nx][ny] == 1:
                count+=1
                map[nx][ny] = 0
                queue.append((nx, ny))
    return count
N = int(input())

map = [list(map( int, input())) for _ in range(N)]
count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result= []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            result.append(bfs(i,j))
print(len(result))
result.sort()
for i in result:
    print(i)