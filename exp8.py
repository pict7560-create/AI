

# DFS Program

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []
stack = ['A']

while stack:
    node = stack.pop()

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in reversed(graph[node]):
            stack.append(neighbour)
