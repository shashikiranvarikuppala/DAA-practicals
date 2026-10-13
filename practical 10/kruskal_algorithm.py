
# Kruskal's Algorithm in Python
# To find the Minimum Spanning Tree (MST)

def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])

    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == len(vertices) - 1:
                break

    if len(mst) != len(vertices) - 1:
        print("The graph is disconnected; MST does not exist.")
        return

    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")

    print("Total Minimum Cost:", total_cost)


# Example graph
vertices = ['A', 'B', 'C', 'D', 'E']

# Each edge contains (vertex1, vertex2, weight)
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5),
    ('C', 'E', 6),
    ('D', 'E', 2)
]

kruskal(vertices, edges)
