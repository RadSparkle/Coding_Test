from collections import deque

def dfs(graph, start):
    visited = set()

    queue = deque([start])
    count=-1
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            count+=1
            for neighor in range(len(graph[node])):
                if graph[node][neighor] and neighor not in visited:
                    queue.append(neighor)
    return count
n = int(input())
m = int(input())
graph = [[0 for i in range(n+1)] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

print(dfs(graph, 1))