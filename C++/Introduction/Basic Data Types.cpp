// Written: 02-Apr-2020
// https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int myInt;
    long myLong;
    char myChar;
    float myFloat;
    double myDouble;
    
    scanf("%d %ld %c %f %lf", &myInt,&myLong,&myChar,&myFloat,&myDouble);
    printf("%d\n%ld\n%c\n%f\n%lf\n", myInt,myLong,myChar,myFloat,myDouble);
    return 0;
}
