#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

// Function for DFS traversal
void dfs(vector<vector<int>>& graph, int start_vertex) {
    int num_vertices = graph.size();
    vector<bool> visited(num_vertices, false);
    stack<int> stk;

    stk.push(start_vertex);
    visited[start_vertex] = true;

    while (!stk.empty()) {
        int curr_vertex = stk.top();
        stk.pop();
        cout << curr_vertex << " ";

        for (int neighbor : graph[curr_vertex]) {
            if (!visited[neighbor]) {
                stk.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }
}

// Function for BFS traversal
void bfs(vector<vector<int>>& graph, int start_vertex) {
    int num_vertices = graph.size();
    vector<bool> visited(num_vertices, false);
    queue<int> que;

    que.push(start_vertex);
    visited[start_vertex] = true;

    while (!que.empty()) {
        int curr_vertex = que.front();
        que.pop();
        cout << curr_vertex << " ";

        for (int neighbor : graph[curr_vertex]) {
            if (!visited[neighbor]) {
                que.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }
}

int main() {
    int num_vertices, num_edges;
    cout << "Enter the number of vertices: ";
    cin >> num_vertices;
    cout << "Enter the number of edges: ";
    cin >> num_edges;

    vector<vector<int>> graph(num_vertices);

    cout << "Enter the edges (format: source destination):" << endl;
    for (int i = 0; i < num_edges; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int start_vertex;
    int choice;
    while (true) {
        cout << "\n1. Perform DFS traversal" << endl;
        cout << "2. Perform BFS traversal" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter the start vertex: ";
                cin >> start_vertex;
                cout << "DFS Traversal: ";
                dfs(graph, start_vertex);
                cout << endl;
                break;
            case 2:
                cout << "Enter the start vertex: ";
                cin >> start_vertex;
                cout << "BFS Traversal: ";
                bfs(graph, start_vertex);
                cout << endl;
                break;
            case 3:
                cout << "Exiting..." << endl;
                return 0;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
