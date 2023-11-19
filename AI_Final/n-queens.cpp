#include <bits/stdc++.h>
using namespace std;

void solve(int col, vector<string> &board, vector<vector<string>> &ans, vector<int> &leftRow, vector<int> &upperDiag, vector<int> &lowerDiag, int n)
{
    if (col == n)
    {
        ans.push_back(board);
        return;
    }
    for (int row = 0; row < n; row++)
    {
        if (leftRow[row] == 0 && lowerDiag[row + col] == 0 && upperDiag[n - 1 + col - row] == 0)
        {
            board[row][col] = 'Q';
            leftRow[row] = lowerDiag[row + col] = upperDiag[n - 1 + col - row] = 1;
            solve(col + 1, board, ans, leftRow, upperDiag, lowerDiag, n);
            board[row][col] = '.';
            leftRow[row] = lowerDiag[row + col] = upperDiag[n - 1 + col - row] = 0;
        }
    }
}

vector<vector<string>> solveNQueens(int n)
{
    vector<vector<string>> ans;
    vector<string> board(n);
    string s(n, '.');
    for (int i = 0; i < n; ++i)
    {
        board[i] = s;
    }
    vector<int> leftRow(n, 0), upperDiag(2 * n - 1, 0), lowerDiag(2 * n - 1, 0);

    solve(0, board, ans, leftRow, upperDiag, lowerDiag, n);

    return ans;
}

int main()
{

    cout << "Enter the size of the board : ";
    int n;
    cin >> n;
    vector<vector<string>> NQueen = solveNQueens(n);

    cout << "The " << n << " Queens are placed as below\n";
    for (int i = 0; i < NQueen.size(); ++i)
    {
        for (int j = 0; j < NQueen[i].size(); ++j)
        {
            string s = NQueen[i][j];
            for (int k = 0; k < s.size(); ++k)
            {
                cout << " " << s[k];
            }
            cout << endl;
        }
        break;
        cout << endl;
    }
}