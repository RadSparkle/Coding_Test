from collections import deque

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    n = len(graph)
    cnt=1
    graph[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx< 0 or ny < 0 or nx>=n or ny>= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt+=1
    return cnt

n = int(input())
graph=[]
group_cnt=0
answer=[]
for _ in range(n):
    graph.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(graph,i,j))

print(len(answer))
answer.sort()
for i in answer:
    print(i)
