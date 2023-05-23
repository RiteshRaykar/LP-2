def is_safe(graph, colors, node, color):
    for i in range(len(graph)):
        if graph[node][i] and colors[i] == color:
            return False
    return True

def graph_coloring(graph, num_colors):
    num_nodes = len(graph)
    colors = [0] * num_nodes

    def backtrack(node):
        if node == num_nodes:
            return True

        for color in range(1, num_colors + 1):
            if is_safe(graph, colors, node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0

        return False

    if backtrack(0):
        return colors
    else:
        return None


# Get user input for the graph
num_nodes = int(input("Enter the number of nodes in the graph: "))
graph = []
for i in range(num_nodes):
    row = list(map(int, input(f"Enter the adjacency matrix row for node {i + 1}: ").split()))
    graph.append(row)

# Get user input for the number of colors
num_colors = int(input("Enter the number of colors: "))

# Solve the graph coloring problem
solution = graph_coloring(graph, num_colors)

# Print the solution if found
if solution:
    print("Solution found:")
    print(solution)
else:
    print("No solution found.")
