n, m, v = map(int, input().split())

graph = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]



def dfs(start):
    stack = [start]
    visited = []
    
    while stack:
        start = stack.pop(0)
        visited.append(start)

        if start in graph:
            next_nodes = sorted(graph[start])
            for i in next_nodes:
                if i not in visited:
                    stack.append(i)
                    break
    
    return visited

def bfs(start):
    queue = [start]
    visited = []

    while queue:
        start = queue.pop()
        visited.append(start)

        if start in graph:
            next_nodes = sorted(graph[start])
            for i in next_nodes:
                if i not in visited:
                    queue.append(i)
                    break
    return visited

for d in dfs(v):
    print(d, end=' ')
print()
for b in bfs(v):
    print(b, end=' ')