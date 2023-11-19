#include <bits/stdc++.h>
using namespace std;

struct Edge
{
    int src, dest, weight;
};

struct Graph
{
    int V, E;
    vector<Edge> edges;

    Graph(int v, int e)
    {
        V = v;
        E = e;
    }
};

int findParent(int node, vector<int> &parent)
{
    if (parent[node] == -1)
        return node;
    return findParent(parent[node], parent);
}

bool comp(Edge a, Edge b)
{
    return a.weight < b.weight;
}

void kruskalsMST(Graph G)
{
    vector<Edge> result;
    vector<int> parent(G.V, -1);

    sort(G.edges.begin(), G.edges.end(), comp);

    int edgeCount = 0;
    int ind = 0;
    while (edgeCount < G.V - 1)
    {
        Edge nextEdge = G.edges[ind++];

        int x = findParent(nextEdge.src, parent);
        int y = findParent(nextEdge.dest, parent);

        if (x != y)
        {
            result.push_back(nextEdge);
            parent[x] = y;
            edgeCount++;
        }
    }

    int minCost = 0;
    for (const Edge &edge : result)
    {
        cout << edge.src << " " << edge.dest << " -> " << edge.weight << endl;
        minCost += edge.weight;
    }

    cout << "minimum cost"
         << " = " << minCost << endl;
}

int main()
{
    int n, e;
    cin >> n >> e;

    Graph G(n, e);

    for (int i = 0; i < e; ++i)
    {
        int u, v, w;
        cin >> u >> v >> w;
        Edge edge;
        edge.src = u;
        edge.dest = v;
        edge.weight = w;

        G.edges.push_back(edge);
    }

    kruskalsMST(G);
}

/*
4 number of vertics 
5 number of edges
0 1 10   (source, destination, weight)
1 3 15
2 3 4 
2 0 6 
0 3 5
2 3 -> 4
0 3 -> 5
0 1 -> 10
minimum cost = 19
*/