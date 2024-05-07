
#1. Identificar que estrategia es la adecuada para resolver este problema y por qué? 
 #La estrategia para resolver este problema es el algoritmo de Dijkstra puesto que, este algoritmo
 #nos permite poder recorrer el grafo que se nos da en la imagen del problema en un grafo dirigido y cómo
 #las aristas contienen pesos y se nos pide el camino más óptimo, nosotros podemos utilizar este algoritmo 
 #que nos dará el caminomás optimo.

#Lista de adyacencia del grafo con aristas con pesos
ciudades = ["A", "B", "C", "D", "E", "F", "G","H","I","J","K","S"]
traficoCiudad = [8,6,5,5,3,3,0,7,4,5,3,7]


graph = [
   #A B C D E F G H I J K S
   [0,1,0,1,0,0,0,0,0,0,0,0], #A
   [0,0,0,1,0,0,0,0,0,0,0,0], #B
   [0,0,0,1,1,1,0,0,0,0,0,0], #C
   [0,0,0,0,0,1,0,1,1,0,0,0], #D
   [0,0,0,0,0,0,1,0,0,0,0,0], #E
   [0,0,0,0,0,0,1,0,0,0,0,0], #F
   [0,0,0,0,0,0,0,0,0,0,0,0], #G
   [0,0,0,0,0,0,0,0,1,1,0,0], #H
   [0,0,0,0,0,0,1,0,0,1,1,0], #I
   [0,0,0,0,0,0,0,0,0,0,1,0], #J
   [0,0,0,0,0,0,1,0,0,0,0,0], #K
   [1,1,1,0,0,0,0,0,0,0,0,0]  #S
]

#Costes de aristas entre ciudades
pesos = [
   #A B C D E F G H I J K S
   [0,8,0,5,0,0,0,0,0,0,0,0], #A
   [0,0,0,15,0,0,0,0,0,0,0,0], #B
   [0,0,0,8,20,2,0,0,0,0,0,0], #C
   [0,0,0,0,0,1,0,16,20,0,0,0], #D
   [0,0,0,0,0,0,19,0,0,0,0,0], #E
   [0,0,0,0,0,0,13,0,0,0,0,0], #F
   [0,0,0,0,0,0,0,0,0,0,0,0], #G
   [0,0,0,0,0,0,0,0,1,2,0,0], #H
   [0,0,0,0,0,0,3,0,0,5,13,0], #I
   [0,0,0,0,0,0,0,0,0,0,7,0], #J
   [0,0,0,0,0,0,16,0,0,0,0,0], #K
   [4,10,11,0,0,0,0,0,0,0,0,0]  #S
]


#Gráfica del grafo
import graphviz as gv

def graficarGrafo(graph):
      g = gv.Digraph(format='png')
      for i in range(len(graph)):
         g.node(ciudades[i])
         for j in range(len(graph)):
               if graph[i][j] != 0:
                  g.edge(ciudades[i], ciudades[j], label=str(pesos[i][j]))
      g.view()

graficarGrafo(graph)



#2. Halle la ruta más corta para ir de la ciudad "S" a la ciudad "G".
import heapq as hq

def dijkstraCiudades(graph, pesos, trafico, start, end):
    n = len(graph)
    visitado = [False] * n
    dist = [float('inf')] * n
    prev = [-1] * n
    dist[start] = 0
    pqueue = [(0, start)]

    while pqueue:
        V, u = hq.heappop(pqueue)

        if visitado[u]:
            continue

        visitado[u] = True

        for v, conectado in enumerate(graph[u]):
            if conectado and not visitado[v]:
                ditanciaAntes = dist[v]
                distanciaNueva = dist[u] + pesos[u][v] + trafico[v]

                if distanciaNueva < ditanciaAntes:
                    prev[v] = u
                    dist[v] = distanciaNueva
                    hq.heappush(pqueue, (distanciaNueva, v))

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()

    return path, dist[end]



#Llamando a la función, encontrando el camino entre  "S" y "G" . Para este caso. S es 11 y G es 6
camino, distancia = dijkstraCiudades(graph, pesos,traficoCiudad, 11, 6)

print("El camino más corto entre S y G es: ", camino)
print("La distancia más corta entre S y G es: ", distancia)


#Graficando el camino hallado

def graficarCamino(graph, camino):
      g = gv.Digraph(format='png')
      for i in range(len(graph)):
         g.node(ciudades[i])
         for j in range(len(graph)):
               if graph[i][j] != 0:
                  g.edge(ciudades[i], ciudades[j], label=str(pesos[i][j]))
      for i in range(len(camino) - 1):
         g.edge(ciudades[camino[i]], ciudades[camino[i + 1]], color='red')
      g.view()

graficarCamino(graph, camino)