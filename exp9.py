
# Travelling Salesman Problem

from itertools import permutations

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)
cities = list(range(n))
min_cost = float('inf')
best_route = []

for route in permutations(cities[1:]):
    path = [0] + list(route) + [0]
    total = 0

    for i in range(len(path) - 1):
        total += cost[path[i]][path[i + 1]]

    if total < min_cost:
        min_cost = total
        best_route = path

print("Shortest Route:", best_route)
print("Minimum Cost:", min_cost)
