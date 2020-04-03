// Written: 03-Apr-2020
// https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a, b;

    cin >> a;
    cin >> b;

    string nums[9] = {"one","two","three","four","five","six","seven","eight","nine"};
    
    for (int i=a; i<=b; i++) {
        if (i <= 9) {
            cout << nums[i-1] << endl;
        } else if (i%2 == 0) {
            cout << "even" << endl;
        } else {
            cout << "odd" << endl;
        }
    }
    return 0;
}
