# Water Jug Problem

x = 0
y = 0

while x != 2:
    print("Jug A:", x, "Jug B:", y)

    if x == 0:
        x = 4
    elif y == 3:
        y = 0
    elif x + y <= 3:
        y = x + y
        x = 0
    else:
        x = x - (3 - y)
        y = 3

print("Jug A:", x, "Jug B:", y)
print("2 litres of water is obtained.")
