// Written: 02-Apr-2020
// https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    string nums[9] = {"one","two","three","four","five","six","seven","eight","nine"};
    
    if (n > 9) {
        cout << "Greater than 9";
    } else {
        cout << nums[n-1];
    }
    
    return 0;
}
