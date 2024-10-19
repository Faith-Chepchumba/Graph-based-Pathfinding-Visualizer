import heapq

def dijkstra(graph, start):

pq = [(0, start)]  *# priority queue (min-heap)*

distances = {node: float('inf') for node in graph}

distances[start] = 0

while pq:

current_distance, current_node = heapq.heappop(pq)

if current_distance > distances[current_node]:

continue

for neighbor, weight in graph[current_node].items():

distance = current_distance + weight

if distance < distances[neighbor]:

distances[neighbor] = distance

heapq.heappush(pq, (distance, neighbor))

return distances
