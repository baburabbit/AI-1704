from queue import Queue

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.cannibals > self.missionaries > 0 or (3 - self.cannibals) > (3 - self.missionaries) > 0:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def get_neighbors(current_state):
    neighbors = []
    possible_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for move in possible_moves:
        new_state = State(
            current_state.missionaries - move[0] * current_state.boat,
            current_state.cannibals - move[1] * current_state.boat,
            1 - current_state.boat
        )

        new_state_on_other_side = State(
            current_state.missionaries + move[0] * (1 - current_state.boat),
            current_state.cannibals + move[1] * (1 - current_state.boat),
            1 - current_state.boat
        )

        if new_state.is_valid() and new_state_on_other_side.is_valid():
            neighbors.append(new_state)

    return neighbors

def breadth_first_search():
    initial_state = State(3, 3, 1)
    goal_state = State(0, 0, 0)

    frontier = Queue()
    frontier.put(initial_state)

    came_from = {}
    came_from[initial_state] = None

    while not frontier.empty():
        current_state = frontier.get()

        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state)
                current_state = came_from[current_state]
            path.reverse()
            return path

        for next_state in get_neighbors(current_state):
            if next_state not in came_from:
                frontier.put(next_state)
                came_from[next_state] = current_state

    return None

def print_solution(path):
    for t, state in enumerate(path):
        print(f"Step {t + 1}:")
        print(f"On the side {state.boat} - Missionaries: {state.missionaries}, Cannibals: {state.cannibals}")
        print(f"On the other side {1 - state.boat} - Missionaries: {3 - state.missionaries}, Cannibals: {3 - state.cannibals}")
        print()

if __name__ == "__main__":
    solution_path = breadth_first_search()

    if solution_path:
        print("Solution found!")
        print_solution(solution_path)
    else:
        print("No solution found.")
