from collections import deque

n, m, v= map(int, input().split())

graph=[[]for i in range(n+1)]

for i in range(m):
    x, t= map(int, input().split())
    graph[t].append(x)
    graph[x].append(t)

for i in range(1, n):
    graph[i].sort()

def bfs(start, graph, visited):
    visited[start]= True
    queue= deque([start])

    while queue:
        e= queue.popleft()
        print(e, end=" ")

        for i in graph[e]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def dfs(s, graph, visited):
    visited[s]= True
    print(s, end=" ")

    for i in graph[s]:
        if not visited[i]:
            dfs(i, graph, visited)


visited=[False]*(n+1)
dfs(v, graph, visited)
print()

visited=[False]*(n+1)
bfs(v, graph, visited)