import heapq

# Define the graph
graph = {
    'Mumbai': {'Pune': 150, 'Nashik': 170},
    'Pune': {'Mumbai': 150, 'Nashik': 210, 'Solapur': 250},
    'Nashik': {'Mumbai': 170, 'Pune': 210, 'Aurangabad': 200},
    'Solapur': {'Pune': 250, 'Aurangabad': 290},
    'Aurangabad': {'Nashik': 200, 'Solapur': 290, 'Nagpur': 450},
    'Nagpur': {'Aurangabad': 450}
}

def heuristic(node, goal):
    # Simple heuristic: Straight-line distance between cities (in km)
    coordinates = {
        'Mumbai': (0, 0),
        'Pune': (120, 0),
        'Nashik': (60, 100),
        'Solapur': (200, 0),
        'Aurangabad': (120, 150),
        'Nagpur': (300, 150)
    }
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def a_star(start, goal):
    # Priority queue to store nodes with their respective costs
    queue = [(0, start)]
    # Dictionary to track the cost of reaching each node from the start node
    cost_so_far = {start: 0}

    while queue:
        # Get the node with the minimum cost so far
        current_cost, current_node = heapq.heappop(queue)

        # If the goal node is reached, return the total cost
        if current_node == goal:
            return cost_so_far[current_node]

        # Explore neighbors of the current node
        for neighbor, cost in graph[current_node].items():
            # Calculate the new cost to reach the neighbor via the current node
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                # Update the cost and priority of the neighbor
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(queue, (priority, neighbor))

    # If the goal node is unreachable, return infinity
    return float('inf')

# Get user input for start and goal nodes
start = input("Enter the start city: ")
goal = input("Enter the goal city: ")

# Test the algorithm
distance = a_star(start, goal)
if distance == float('inf'):
    print("No path found between the cities.")
else:
    print(f"The distance between {start} and {goal} is {distance} km.")
