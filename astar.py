def astar(G, s, t, h): # A*
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    g = [math.inf]*n
    q = []
    f = lambda u: g[u] + h[u]
    heapq.heappush(q, (f(s), s))
    g[s] = 0

    while q:
        _, u = heapq.heappop(q)
        if visited[u]:
            continue
        visited[u] = True
        if u == t:
            break
        for v, w in G[u]:
            if not visited[v] and g[u] + w < g[v]:
                g[v] = g[u] + w
                path[v] = u
                heapq.heappush(q, (f(v), v))

    return path, g


def dijkstra(G, s, t):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    g = [math.inf]*n
    q = []
    heapq.heappush(q, (0, s))
    g[s] = 0

    while q:
        _, u = heapq.heappop(q)
        if visited[u]:
            continue
        visited[u] = True
        if u == t:
            break
        for v, w in G[u]:
            if not visited[v] and g[u] + w < g[v]:
                g[v] = g[u] + w
                path[v] = u
                heapq.heappush(q, (g[v], v))

    return path, g