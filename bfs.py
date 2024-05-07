def bfs(G, s):
    n = len(G)
    visited = [False]*n
    parents = [-1]*n
    queue = [s]
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                queue.append(v)

    return parents