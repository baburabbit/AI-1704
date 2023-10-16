import heapq

class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

def print_solution(node):
    path = []
    while node is not None:
        path.append(node.board)
        node = node.parent
    path.reverse()
    for state in path:
        for row in state:
            print(" ".join(map(str, row)))
        print()

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_neighbors(state):
    neighbors = []
    x, y = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y):
            neighbor = [row[:] for row in state]
            neighbor[x][y], neighbor[new_x][new_y] = neighbor[new_x][new_y], neighbor[x][y]
            neighbors.append(neighbor)
    return neighbors

def heuristic(state, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                h += 1
    return h

def solve_puzzle(initial_state, goal_state):
    open_set = []
    closed_set = set()
    start_node = PuzzleState(initial_state, None, None, 0, 0)
    heapq.heappush(open_set, start_node)
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.board == goal_state:
            print("Solution found!")
            print_solution(current_node)
            return
        closed_set.add(tuple(map(tuple, current_node.board)))
        neighbors = get_neighbors(current_node.board)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor)) not in closed_set:
                move = current_node.move
                if move is not None:
                    move += 1
                new_cost = current_node.cost + 1
                new_depth = current_node.depth + 1
                new_node = PuzzleState(neighbor, current_node, move, new_depth, new_cost + heuristic(neighbor, goal_state))
                heapq.heappush(open_set, new_node)
    print("No solution found.")

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
    goal_state = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
    solve_puzzle(initial_state, goal_state)
