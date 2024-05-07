#implementa kosaraju 

def kosaraju(G):
    # Inicializa as variáveis
    n = len(G)
    visited = [False] * n
    stack = []
    scc = []
    # Função para visitar os vértices
    def visit(v):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                visit(u)
        stack.append(v)
    # Visita os vértices
    for v in range(n):
        if not visited[v]:
            visit(v)
    # Inverte o grafo
    GT = [[] for _ in range(n)]
    for v in range(n):
        for u in G[v]:
            GT[u].append(v)
    visited = [False] * n
    # Função para visitar os vértices
    def visit(v):
        visited[v] = True
        scc[-1].append(v)
        for u in GT[v]:
            if not visited[u]:
                visit(u)
    # Visita os vértices
    while stack:
        v = stack.pop()
        if not visited[v]:
            scc.append([])
            visit(v)
    return scc

def main():
    # Grafo de exemplo
    G = [[1], [2], [0], [4], [3], [5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 15], [14, 16], [15, 17], [16, 18], [17, 19], [18, 20], [19, 21], [20, 22], [21, 23], [22, 24], [23, 25], [24, 26], [25, 27], [26, 28], [27, 29], [28, 30], [29, 31], [30, 32], [31, 33], [32, 34], [33, 35], [34, 36], [35, 37], [36, 38], [37, 39], [38, 40], [39, 41], [40, 42], [41, 43], [42, 44], [43, 45], [44, 46], [45, 47], [46, 48], [47, 49], [48, 50], [49], [50], []]
    
    print(kosaraju(G))
