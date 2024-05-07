def dfs(G, s):
    n = len(G)
    visited = [False]*n
    parents = [-1]*n

    def _dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                _dfs(v)

    _dfs(s)

    return parents


def lds(G, s, L):
    n = len(G)
    visited = [False]*n
    parents = [-1]*n

    def _dfs(u, l):
        if l == 0: return
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                _dfs(v, l - 1)

    _dfs(s, L)

    return parents


def ids(G, s, t):
    n = len(G)
    for L in range(1, n+1):
        path = lds(G, s, L)
        if path[t] != -1:
            break
    return path, L

def dijkstra(G, s):
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
        for v, w in G[u]:
            if not visited[v] and g[u] + w < g[v]:
                g[v] = g[u] + w
                path[v] = u
                heapq.heappush(q, (g[v], v))

    return path, g