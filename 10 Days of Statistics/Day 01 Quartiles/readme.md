# Day 1: Quartiles

## Objective
In this challenge, we practice calculating quartiles. Check out the [Tutorial](https://www.hackerrank.com/challenges/s10-quartiles/tutorial) tab for learning materials and an instructional video!

## Task
Given an array, **_X_**, of **_n_** integers, calculate the respective first quartile (**_Q<sub>1</sub>_**), second quartile (**_Q<sub>2</sub>_**), and third quartile (**_Q<sub>3</sub>_**). It is guaranteed that **_Q<sub>1</sub>_**, **_Q<sub>2</sub>_**, and **_Q<sub>3</sub>_** are integers.

## Input Format
The first line contains an integer, **_n_**, denoting the number of elements in the array.<br>
The second line contains **_n_** space-separated integers describing the array's elements.

## Constraints
* **_5 &le; n &le; 50_**
* **_0 &lt; x<sub>i</sub> &le; 100_**, where x<sub>i</sub> is the i<sup>th</sup> element of the array.

## Output Format
Print **_5_** lines of output in the following order:
1. The first line should be the value of **_Q<sub>1</sub>_**.
2. The second line should be the value of **_Q<sub>2</sub>_**.
3. The third line should be the value of **_Q<sub>3</sub>_**.

## Sample Input
```
9
3 7 8 5 12 14 21 13 18
```

## Sample Output
```
6
12
16
```

## Explanation
**_X_ = {3,7,8,5,12,14,21,13,18}**. When we sort the elements in non-decreasing order, we get **_X_ = {3,5,7,8,12,13,14,18,21}**. It's easy to see that **_median(X)_ = 12**.

As there are an odd number of data points, we do not include the median (the central value in the ordered list) in either half:
```
Lower half (L): 3, 5, 7, 8
Upper half (U): 13, 14, 18, 21
```
Now, we find the quartiles:

* **_Q<sub>1</sub>_** is the **_median(L)_**. So, **_Q<sub>1</sub>_ = (5+7)/2 = 6**
* **_Q<sub>1</sub>_** is the **_median(L)_**. So, **_Q<sub>2</sub>_ = 12**
* **_Q<sub>1</sub>_** is the **_median(L)_**. So, **_Q<sub>3</sub>_ = (14+18)/2 = 16**