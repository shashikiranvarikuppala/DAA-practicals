from collections import deque
import time

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            # Add unvisited adjacent vertices to queue
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)


# Graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting vertex
start_vertex = 'A'

# Measure execution time
start_time = time.perf_counter()

print("BFS Traversal:")
bfs(graph, start_vertex)

end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

print("\nExecution Time:", execution_time, "seconds")

# Complexity
print("Time Complexity: O(V + E)")
print("Space Complexity: O(V)")