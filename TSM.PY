import itertools

def calculate_total_distance(order, cities):
    total_distance = 0
    num_cities = len(order)
    for i in range(num_cities):
        from_city = order[i]
        to_city = order[(i + 1) % num_cities]
        total_distance += cities[from_city][to_city]
    return total_distance

def traveling_salesman_bruteforce(cities):
    num_cities = len(cities)
    city_indices = list(range(num_cities))
    best_order = None
    best_distance = float('inf')

    for order in itertools.permutations(city_indices):
        total_distance = calculate_total_distance(order, cities)
        if total_distance < best_distance:
            best_distance = total_distance
            best_order = order

    return best_order, best_distance

if __name__ == '__main__':
    # Example usage
    cities = [
        [0, 29, 20, 21],
        [29, 0, 15, 17],
        [20, 15, 0, 28],
        [21, 17, 28, 0]
    ]
    best_order, best_distance = traveling_salesman_bruteforce(cities)

    print("Best order:", best_order)
    print("Best distance:", best_distance)
