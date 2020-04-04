# Day 0: Mean, Median, and Mode

## Objective
In this challenge, we practice calculating the mean, median, and mode. Check out the [Tutorial](https://www.hackerrank.com/challenges/s10-basic-statistics/tutorial) tab for learning materials and an instructional video!

## Task
Given an array, **_X_**, of **_N_** integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

**_Note_**: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of **_1_** decimal place (i.e., **_12.3_**, **_7.0_** format).

## Input Format
The first line contains an integer, **_N_**, denoting the number of elements in the array.
The second line contains **_N_** space-separated integers describing the array's elements.

## Constraints
* **_10 &le; N &le; 2500_**
* **_0 &lt; x<sub>i</sub> 10<sup>5</sup>_**, where **_x<sub>i</sub>_** is the **_i<sup>th</sup>_** element of the array.

## Output Format
Print **_3_** lines of output in the following order:
1. Print the mean on a new line, to a scale of **_1_** decimal place (i.e., **_12.3_**, **_7.0_** format).
2. Print the median on a new line, to a scale of **_1_** decimal place (i.e., **_12.3_**, **_7.0_** format).
3. Print the mode on a new line; if more than one such value exists, print the numerically smallest one.

## Sample Input
```
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
```

## Sample Output
```
43900.6
44627.5
4978
```

## Explanation
<strong>Mean</strong>\
We sum all
elements in the array, divide the sum by **_N_**, and print our result on a new line.
![img](http://www.sciweavers.org/tex2img.php?eq=%20%5Cmu%20%3D%20%20%5Cfrac%7Bx_%7B0%7D%2Bx_%7B1%7D%2Bx_%7B2%7D%2Bx_%7B3%7D%2Bx_%7B4%7D%2Bx_%7B5%7D%2Bx_%7B6%7D%2Bx_%7B7%7D%2Bx_%7B8%7D%2Bx_%7B9%7D%7D%7B10%7D%20%20%3D%20%20%5Cfrac%7B439006%7D%7B10%7D%20%3D%2043900.6&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

<strong>Median</strong>:\
To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order. The sorted array **_X_ = {4978, 11735, 14216, 14470, 38120, 51135, 6463O, 73429, 99233}**. We then average the two middle elements:
and print our result on a new line.
![img](http://www.sciweavers.org/tex2img.php?eq=median%20%3D%20%20%20%5Cfrac%7B%20x_%7B4%7D%20%2B%20%20x_%7B5%7D%7D%7B2%7D%20%3D%20%20%5Cfrac%7B89255%7D%7B2%7D%20%3D%2044627.5%20%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

<strong>Mode</strong>:\
We can find the number of occurrences of all the elements in the array:
```
 4978 : 1
11735 : 1
14216 : 1
14470 : 1
38120 : 1
51135 : 1
64630 : 1
67060 : 1
73429 : 1
99233 : 1
```
Every number occurs once, making **_1_** the maximum number of occurrences for any number in **_X_**. Because we have multiple values to choose from, we want to select the smallest one, **_4978_**, and print it on a new line.