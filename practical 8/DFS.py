import time

# DFS function
def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)

        # Visit all adjacent vertices
        for neighbour in graph[vertex]:
            dfs(graph, neighbour, visited)


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

# Set to store visited vertices
visited = set()

# Measure execution time
start_time = time.perf_counter()

print("DFS Traversal:")
dfs(graph, start_vertex, visited)

end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

print("\nExecution Time:", execution_time, "seconds")

# Complexity
print("Time Complexity: O(V + E)")
print("Space Complexity: O(V)")