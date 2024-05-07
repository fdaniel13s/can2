import heapq as hq
import math

def dijkstra(Graph, start, end):
    n = len(Graph)
    visited = [False] * n
    cost = [math.inf] * n
    cost[start] = 0
    pqueue = [(0, start)]

    while pqueue:
        g, u = hq.heappop(pqueue)
        if u == end:
            return g
        if not visited[u]:
            visited[u] = True
            for vecino, peso in Graph[u]:
                if not visited[vecino]:
                    newCost = g + peso
                    if newCost < cost[vecino]:
                        cost[vecino] = newCost
                        hq.heappush(pqueue, (newCost, vecino))
    return "NINGUNO"

def main():
    with open('input1.txt', 'r') as file:
        num_tests = int(file.readline().strip())
        results = []
        
        for _ in range(num_tests):
            n, m, start_city, end_city = map(int, file.readline().strip().split())
            Graph = [[] for _ in range(n + 1)]
            
            for __ in range(m):
                u, v, t = map(int, file.readline().strip().split())
                Graph[u].append((v, t))
                Graph[v].append((u, t))
            
            print(Graph)
            # Corregir índices ya que dijkstra espera índices desde 0, si no es tu caso, omitir -1.
            result = dijkstra(Graph, start_city, end_city)
            results.append(result)
        
        for result in results:
            print(result)

if __name__ == "__main__":
    main()



# Red de transporte de Carga
import heapq as hq
import math

def dijkstra(Graph, start, end):
    n = len(Graph)
    visited = [False] * n
    costTiempo = [math.inf] * n
    costTiempo[start] = 0
    costPeso = [0] * n
    costPeso[start] = float('inf')
    pqueue = [(0, start,float('inf'))]

    while pqueue:
        tiempo_actual, u, peso_actual = hq.heappop(pqueue)
        if u == end:
            return tiempo_actual,peso_actual
        if not visited[u]:
            visited[u] = True
            for vecino, tiempo,peso in Graph[u]:
                if not visited[vecino]:
                    newCostT = tiempo_actual + tiempo
                    newCostP = min(peso_actual,peso)
                    if newCostT < costTiempo[vecino]:
                        costTiempo[vecino] = newCostT
                        costPeso[vecino] = newCostP
                        hq.heappush(pqueue, (newCostT, vecino,newCostP))
                    elif newCostT == costTiempo[vecino] and newCostP > costPeso[vecino]:
                        costPeso[vecino] = newCostP
                        hq.heappush(pqueue, (newCostT, vecino,newCostP))
                    
    return "NINGUNO"


def main():
    with open('input2.txt', 'r') as file:
        num_tests = int(file.readline().strip())
        results = []
        
        for _ in range(num_tests):
            n, m = map(int, file.readline().strip().split())
            start_city, end_city = map(int, file.readline().strip().split())

            Graph = [[] for _ in range(n + 1)]
            
            for __ in range(m):
                u, v, t ,p = map(int, file.readline().strip().split())
                Graph[u].append((v, t,p))
                Graph[v].append((u, t,p))
            
            print(Graph)
            # Corregir índices ya que dijkstra espera índices desde 0, si no es tu caso, omitir -1.
            result = dijkstra(Graph, start_city, end_city)
            results.append(result)

            if result == "NINGUNO":
                print("NINGUNO")
            else:
                tiempo,peso = result
                print(tiempo,peso)
    

if __name__ == "__main__":
    main()
