# Day 1: Interquartile Range

## Objective
In this challenge, we practice calculating the interquartile range. We recommend you complete the [Quartiles](https://www.hackerrank.com/challenges/s10-quartiles) challenge before attempting this problem.

## Task
The interquartile range of an array is the difference between its first (**_Q<sub>1</sub>_**) and third (**_Q<sub>3</sub>_**) quartiles (i.e.,**_Q<sub>3</sub> - Q<sub>1</sub>_**).

Given an array, **_X_**, of **_n_** integers and an array, **_F_**, representing the respective frequencies of **_X_**'s elements, construct a data set, **_S_**, where each **_x<sub>i</sub>_** occurs at frequency **_f<sub>i</sub>_**. Then calculate and print **_S_**'s interquartile range, rounded to a scale of **1** decimal place (i.e., **12.3** format).

**Tip**: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

## Input Format

The first line contains an integer, **_n_**, denoting the number of elements in arrays **_X_** and **_F_**.\
The second line contains **_n_** space-separated integers describing the respective elements of array **_X_**.\
The third line contains **_n_** space-separated integers describing the respective elements of array **_F_**.

## Output Format
Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of **1** decimal place (i.e., **12.3** format).

## Sample Input
```
6
6 12 8 10 20 16
5 4 3 2 1 5
```

## Sample Output
```
9.0
```
