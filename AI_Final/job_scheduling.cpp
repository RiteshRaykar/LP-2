#include <bits/stdc++.h>
using namespace std;

struct Job
{
    int start, finish, profit;
};

bool jobComparator(Job s1, Job s2)
{
    return (s1.finish < s2.finish);
}

int firstNonConflict(vector<Job> &v, int i)
{
    for (int j = i - 1; j >= 0; j--)
    {
        if (v[j].finish <= v[i - 1].start)
            return j;
    }
    return -1;
}

int func(vector<Job> &v, int n)
{
    if (n == 1)
        return v[n - 1].profit;

    int inclProf = v[n - 1].profit;
    int i = firstNonConflict(v, n);
    if (i != -1)
        inclProf += func(v, i + 1);

    int exclProf = func(v, n - 1);

    return max(inclProf, exclProf);
}

int findMaxProfit(vector<Job> v, int n)
{
    sort(v.begin(), v.end(), jobComparator);

    return func(v, n);
}

int main()
{
    vector<Job> v = {{1, 2, 10}, {1, 3, 20}, {3, 5, 30}, {4, 6, 40}, {5, 7, 50}, {6, 8, 60}, {7, 9, 70}, {8, 10, 80}, {9, 11, 90}, {10, 12, 100}};
    int n = v.size();
    cout << "The optimal profit is " << findMaxProfit(v, n);
    return 0;
}