#include <iostream>
using namespace std;
int findMin(int a, int b)
{
    if (a < b)
    {
        return a;
    }
    return b;
}
int main
{
    int n = 4;
    int d[4][4];
    int x[n] = {1, 10, 10, 1};
    int f[n] = {1, 2, 4, 8};

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if (i == j)
            d[i][j] = findMin(x[i], )
        }
    }
    return 0;
}