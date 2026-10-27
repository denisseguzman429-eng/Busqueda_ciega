import time
from collections import deque

# Representación del grafo (Laberinto simple)
laberinto = {
    'Inicio': ['A', 'B'],
    'A': ['Inicio', 'C', 'D'],
    'B': ['Inicio', 'E'],
    'C': ['A'],
    'D': ['A', 'F'],
    'E': ['B', 'F'],
    'F': ['D', 'E', 'Meta'],
    'Meta': ['F']
}

def bfs(grafo, inicio, meta):
    cola = deque([(inicio, [inicio])]) # Almacena (nodo_actual, camino_hasta_ahora)
    visitados = set([inicio])
    nodos_expandidos = 0
    
    while cola:
        nodo_actual, camino = cola.popleft()
        nodos_expandidos += 1
        
        if nodo_actual == meta:
            return camino, nodos_expandidos
            
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))
                
    return None, nodos_expandidos

def dfs(grafo, inicio, meta):
    pila = [(inicio, [inicio])]
    visitados = set()
    nodos_expandidos = 0
    
    while pila:
        nodo_actual, camino = pila.pop()
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            nodos_expandidos += 1
            
            if nodo_actual == meta:
                return camino, nodos_expandidos
                
            # Agregamos vecinos a la pila. Invertimos para explorar en orden alfabético.
            for vecino in reversed(grafo.get(nodo_actual, [])):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino]))
                    
    return None, nodos_expandidos

# --- Ejecución y Comparación ---
nodo_inicio = 'Inicio'
nodo_meta = 'Meta'

# Ejecutar y medir BFS
inicio_tiempo = time.perf_counter()
camino_bfs, exp_bfs = bfs(laberinto, nodo_inicio, nodo_meta)
tiempo_bfs = time.perf_counter() - inicio_tiempo

# Ejecutar y medir DFS
inicio_tiempo = time.perf_counter()
camino_dfs, exp_dfs = dfs(laberinto, nodo_inicio, nodo_meta)
tiempo_dfs = time.perf_counter() - inicio_tiempo

# Imprimir Resultados (Camino solución y comparación)
print("=== Resultados de la Búsqueda ===")
print(f"BFS | Nodos expandidos: {exp_bfs} | Tiempo: {tiempo_bfs:.6f} s")
print(f"Camino BFS: {' -> '.join(camino_bfs)}\n")

print(f"DFS | Nodos expandidos: {exp_dfs} | Tiempo: {tiempo_dfs:.6f} s")
print(f"Camino DFS: {' -> '.join(camino_dfs)}")