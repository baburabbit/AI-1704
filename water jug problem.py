def min_moves(x, y, z):
    if x == y:
        return z
    if x < y:
        return min_moves(z, y, x)
    if x > y:
        return min_moves(x - y, y, z) + y

def solve_water_jug_problem(x, y, z):
    if x + y < z:
        return "Can't measure exactly " + str(z) + " liters using these jugs."
    if x == y and x == z:
        return "All jugs are already full."
    if x == y and x == 0:
        return "All jugs are already empty."
    if x == z:
        return "Measure exactly " + str(z) + " liters into the first jug."
    if y == z:
        return "Measure exactly " + str(z) + " liters into the second jug."
    if x == 0:
        return "Measure exactly " + str(z) + " liters from the second jug into the first jug."
    if y == 0:
        return "Measure exactly " + str(z) + " liters from the first jug into the second jug."
    if x > y:
        return "Measure exactly " + str(y) + " liters from the first jug into the second jug. Then, measure exactly " + str(z - y) + " liters from the second jug into the first jug."
    if y > x:
        return "Measure exactly " + str(x) + " liters from the second jug into the first jug. Then, measure exactly " + str(z - x) + " liters from the first jug into the second jug."

x = 4
y = 3
z = 2

print(solve_water_jug_problem(x, y, z))
