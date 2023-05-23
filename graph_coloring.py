class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_coloring_util(self, m, color, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring_util(m, color, v + 1):
                    return True
                color[v] = 0

    def graph_coloring(self, m):
        color = [0] * self.V
        if not self.graph_coloring_util(m, color, 0):
            print("No solution exists.")
            return False

        print("The graph can be colored with", m, "colors.")
        print("Color assignment for each vertex:")
        for v in range(self.V):
            print("Vertex", v + 1, ":", color[v])

        return True


# Taking input from the user
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

graph = Graph(num_vertices)

print("Enter the connections between vertices (e.g., '1 2' for an edge between vertex 1 and vertex 2): ")
for _ in range(num_edges):
    edge = input().split()
    v1, v2 = map(int, edge)
    graph.graph[v1 - 1][v2 - 1] = 1
    graph.graph[v2 - 1][v1 - 1] = 1

num_colors = int(input("Enter the number of colors available: "))

graph.graph_coloring(num_colors)
