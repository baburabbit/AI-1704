def min_moves(x, y, z):
    if x == z or y == z or x + y == z:
        return 0
    if x == 0 or y == 0:
        return "Can't measure exactly " + str(z) + " liters using these jugs."
    if x < y:
        return min_moves(x, y - x, z) + 1
    else:
        return min_moves(x - y, y, z) + 1

def solve_water_jug_problem(x, y, z):
    if x + y < z:
        return "Can't measure exactly " + str(z) + " liters using these jugs."
    if x == z:
        return "Measure exactly " + str(z) + " liters into the first jug."
    if y == z:
        return "Measure exactly " + str(z) + " liters into the second jug."
    moves = min_moves(x, y, z)
    return f"Measure exactly {z} liters using {moves} moves."

x = 4
y = 3
z = 0

print(solve_water_jug_problem(x, y, z))
