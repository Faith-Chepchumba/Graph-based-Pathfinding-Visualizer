import heapq

def heuristic(node, goal):

return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(grid, start, goal):

open_set = []

heapq.heappush(open_set, (0, start))

came_from = {}

g_score = {node: float('inf') for row in grid for node in row}

g_score[start] = 0

while open_set:

_, current = heapq.heappop(open_set)

if current == goal:

return reconstruct_path(came_from, current)

for neighbor in current.neighbors:

tentative_g_score = g_score[current] + 1  *# Assuming uniform grid*

if tentative_g_score < g_score[neighbor]:

came_from[neighbor] = current

g_score[neighbor] = tentative_g_score

heapq.heappush(open_set, (g_score[neighbor] + heuristic(neighbor, goal), neighbor))

return False
