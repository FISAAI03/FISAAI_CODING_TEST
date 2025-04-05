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
        start = stack.pop()
        if start not in visited:
            visited.append(start)

        if start in graph:
            next_nodes = sorted(graph[start], reverse=True)
            for i in next_nodes:
                if i not in visited:
                    stack.append(i)
    
    return visited

def bfs(start):
    queue = [start]
    visited = [start]

    while queue:
        start = queue.pop(0)

        if start in graph:
            next_nodes = sorted(graph[start])
            for i in next_nodes:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        
    return visited
    

for d in dfs(v):
    print(d, end=' ')
print()
for b in bfs(v):
    print(b, end=' ')