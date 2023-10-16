from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFSUtil(self, v, visited):
        visited.add(v)
        queue = [v]

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def BFS(self, v):
        visited = set()
        self.BFSUtil(v, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Breadth First Traversal (starting from vertex 0):")
g.BFS(0)
