# Topological Sort using DFS (Without using libraries)

def dfs(v, visited, stack, graph, n):
    visited[v] = 1

    for i in range(n):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i, visited, stack, graph, n)

    stack.append(v)   # Push after visiting all neighbors


def topological_sort():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    # Adjacency Matrix
    graph = [[0 for _ in range(n)] for _ in range(n)]

    print("Enter edges (u v) meaning u -> v:")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u][v] = 1

    visited = [0] * n
    stack = []

    # Call DFS for all unvisited vertices
    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, stack, graph, n)

    print("Topological Order:")
    while len(stack) > 0:
        print(stack.pop(), end=" ")


# Run program
topological_sort()