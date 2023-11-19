#include <bits/stdc++.h>
using namespace std;

bool isValidEdge(int u, int v, vector<bool> inMST)
{
    if (u == v)
        return false;
    if (inMST[u] == false && inMST[v] == false)
        return false;
    else if (inMST[u] == true && inMST[v] == true)
        return false;
    return true;
}

void primMST(vector<vector<int>> cost,int V)
{
    vector<bool> inMST(V, false);

    inMST[0] = true;

    int edge_count = 0, mincost = 0;
    while (edge_count < V - 1)
    {

        int min = INT_MAX, a = -1, b = -1;
        for (int i = 0; i < V; i++)
        {
            for (int j = 0; j < V; j++)
            {
                if (cost[i][j] < min)
                {
                    if (isValidEdge(i, j, inMST))
                    {
                        min = cost[i][j];
                        a = i;
                        b = j;
                    }
                }
            }
        }
        if (a != -1 && b != -1)
        {
            printf("Edge %d:(%d, %d) cost: %d \n",
                   edge_count++, a, b, min);
            mincost = mincost + min;
            inMST[b] = inMST[a] = true;
        }
    }
    printf("\n Minimum cost= %d \n", mincost);
}

int main()
{
    int n, e;
    cin >> n >> e;
    vector<vector<int>> cost(n, vector<int>(n, INT_MAX));
    for (int i = 0; i < e; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        cost[u][v] = w;
        cost[v][u] = w;
    }

    primMST(cost,n);

    return 0;
}
/*
7
11
0 5 8
0 3 3 
5 3 4
0 1 7
1 3 5
5 6 2
3 6 6
3 4 1
1 2 4
2 4 2
6 4 3
3
*/