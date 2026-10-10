start = (3, 3, 1)
goal = (0, 0, 0)

visited = set()
queue = [(start, [])]

moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def safe(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    rm = 3 - m
    rc = 3 - c
    if rm > 0 and rc > rm:
        return False
    return True

while queue:
    state, path = queue.pop(0)

    if state == goal:
        print("Solution:")
        for step in path + [state]:
            print(step)
        break

    if state in visited:
        continue
    visited.add(state)

    m, c, boat = state

    for x, y in moves:
        if boat == 1:
            new_state = (m - x, c - y, 0)
        else:
            new_state = (m + x, c + y, 1)

        if safe(new_state[0], new_state[1]) and new_state not in visited:
            queue.append((new_state, path + [state]))
else:
    print("No solution found")
