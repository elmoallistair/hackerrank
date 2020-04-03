// Written: 04-Apr-2020
// https://www.hackerrank.com/challenges/variable-sized-arrays/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, q;
    cin >> n >> q;
    vector<int> a[n];
    
    int k, temp;
    for (int i=0; i<n; i++) {
      cin >> k;
      for (int j=0; j<k; j++) {
        cin >> temp;
        a[i].push_back(temp);
        }
    }
    
    int i, j;
    for(int k = 1; k <= q; k++){
        cin >> i >> j;
        cout << a[i][j] << endl;
    }

    return 0;
}
