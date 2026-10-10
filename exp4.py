N = 5

start = (1, 1)
goal = (5, 5)

blocked = [(2, 2), (2, 3), (3, 3), (4, 2), (4, 4)]

moves = [
    ("Up", -1, 0),
    ("Down", 1, 0),
    ("Left", 0, -1),
    ("Right", 0, 1)
]

def dfs():
    stack = [start]
    visited = [start]
    parent = {}

    while stack:
        current = stack.pop()

        if current == goal:
            break

        r, c = current

        for name, dr, dc in reversed(moves):
            next_cell = (r + dr, c + dc)

            if (1 <= next_cell[0] <= N and
                1 <= next_cell[1] <= N and
                next_cell not in blocked and
                next_cell not in visited):

                visited.append(next_cell)
                parent[next_cell] = current
                stack.append(next_cell)

    if goal not in visited:
        print("No path found")
        return

    # Create path
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    print("Path:", path)
    print("Cost:", len(path) - 1)


dfs()
