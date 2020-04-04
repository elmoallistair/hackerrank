# Day 0: Weighted Mean

## Objective
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the [Tutorial](https://www.hackerrank.com/challenges/s10-we**_X_**ighted-mean/tutorial) tab for learning materials and an instructional video

## Task
Given an array, **_X_**, of **_N_** integers and an array, **_W_**, representing the respective weights of **_X_**'s elements, calculate and print the weighted mean of **_X_**'s elements. Your answer should be rounded to a scale of **_1_** decimal place (i.e., **_1.23_** format).

## Input Format
The first line contains an integer, **_N_**, denoting the number of elements in arrays **_X_** and **_W_**.\
The second line contains **_N_** space-separated integers describing the respective elements of array **_X_**.\
The third line contains **_N_** space-separated integers describing the respective elements of array **_W_**.

## Constraints
* **_5 &le; N &le; 50_**
* **_0 &lt; w<sub>i</sub> &le; 100_**, where is the element of array **_X_**.
* **_0 &lt; N<sub>i</sub> &le; 100_**, where is the element of array **_W_**.

## Output Format
Print the weighted mean on a new line. Your answer should be rounded to a scale of **_1_** decimal place (i.e., **_12.3_** format).

## Sample Input
```
5
10 40 30 50 20
1 2 3 4 5
```

## Sample Output
```
32.0
```

## Explanation
We use the following formula to calculate the weighted mean:

![img](http://www.sciweavers.org/tex2img.php?eq=%20m_%7Bw%7D%20%3D%20%20%5Cfrac%7B%5Csum_%7Bi%3D0%7D%5E%7BN-1%7D%20%28%20x_%7Bi%7D%20%20%5Ctimes%20%20w_%7Bi%7D%29%7D%7B%5Csum_%7Bi%3D0%7D%5E%7BN-1%7D%20%20w_%7Bi%7D%7D%20%20%5CRightarrow%20%20m_%7Bw%7D%20%3D%20%20%5Cfrac%7B10%20%20%5Ctimes%201%20%2B%2040%20%5Ctimes%202%20%2B%2030%20%5Ctimes%203%20%2B%2050%20%5Ctimes%204%20%2B%2020%20%5Ctimes%205%7D%7B10%7D%20%20%3D%20%20%5Cfrac%7B480%7D%7B15%7D%20%3D%2032.0&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

And then print our result to a scale of **_1_** decimal place (**_32_**) on a new line.