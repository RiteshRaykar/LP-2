#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

void dijkstra(vector<vector<pair<int, int>>> &graph, int source)
{
    int n = graph.size();

    // Create a distance array to store the minimum distance from the source to each vertex
    vector<int> distance(n, INF);

    // Mark the source vertex with a distance of 0
    distance[source] = 0;

    // Create a priority queue to store the vertices and their distances
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, source});

    while (!pq.empty())
    {
        int u = pq.top().second;
        int dist = pq.top().first;
        pq.pop();

        // Skip if the distance to u from the priority queue is greater than the current distance array
        if (dist > distance[u])
            continue;

        // Explore all neighboring vertices of u
        for (auto &neighbor : graph[u])
        {
            int v = neighbor.first;
            int weight = neighbor.second;

            // Relax the edge if a shorter path is found
            if (distance[u] + weight < distance[v])
            {
                distance[v] = distance[u] + weight;
                pq.push({distance[v], v});
            }
        }
    }

    // Print the shortest distances from the source to all vertices
    cout << "Shortest distances from the source vertex " << source << ":\n";
    for (int i = 0; i < n; ++i)
    {
        if (distance[i] == INF)
            cout << i << ": INF\n";
        else
            cout << i << ": " << distance[i] << "\n";
    }
}

int main()
{
    int n, m;
    cout << "Enter the number of vertices: ";
    cin >> n;
    cout << "Enter the number of edges: ";
    cin >> m;

    vector<vector<pair<int, int>>> graph(n);

    cout << "Enter the edges (source, destination, weight):\n";
    for (int i = 0; i < m; ++i)
    {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }

    int source;
    cout << "Enter the source vertex: ";
    cin >> source;

    dijkstra(graph, source);

    return 0;
}


/*
Enter number of vertices:
4
Enter number of edges:
5
Enter edge vertices of edge 1 :
0 1
Enter edge vertices of edge 1 :
0 2
Enter edge vertices of edge 1 :
1 3
Enter edge vertices of edge 1 :
2 3
Enter edge vertices of edge 1 :
0 3
Vertex 0 is coloured 1
Vertex 1 is coloured 2
Vertex 2 is coloured 2
Vertex 3 is coloured 3
*/