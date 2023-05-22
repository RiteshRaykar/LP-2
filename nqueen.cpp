#include <iostream>
#include <vector>
using namespace std;

bool isSafe(const vector<string>& board, int row, int col) {
    int n = board.size();
    for (int i = 0; i < col; i++) {
        if (board[row][i] == 'Q') return false;
        if (row - col + i >= 0 && board[row - col + i][i] == 'Q') return false;
        if (row + col - i < n && board[row + col - i][i] == 'Q') return false;
    }
    return true;
}

void solveNQueensUtil(vector<vector<string>>& result, vector<string>& board, int col) {
    int n = board.size();
    if (col == n) {
        result.push_back(board);
        return;
    }
    for (int row = 0; row < n; row++) {
        if (isSafe(board, row, col)) {
            board[row][col] = 'Q';
            solveNQueensUtil(result, board, col + 1);
            board[row][col] = '.';
        }
    }
}

vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> result;
    vector<string> board(n, string(n, '.'));
    solveNQueensUtil(result, board, 0);
    return result;
}

int main() {
    int n;
    cout << "Enter the number of queens: ";
    cin >> n;
    vector<vector<string>> solutions = solveNQueens(n);
    for (const auto& board : solutions) {
        for (const auto& row : board) {
            cout << row << endl;
        }
        cout << endl;
    }
    return 0;
}