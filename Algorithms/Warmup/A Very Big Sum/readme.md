## A Very Big Sum
Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

### Function Description
Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):
* ar: an array of integers .

### Input Format
The first line of the input consists of an integer ***n***.
The next line contains ***n*** space-separated integers contained in the array.

### Output Format
Print the integer sum of the elements in the array.

### Constraints
* **1 &le; _n_ &le; 10**
* **1 &le; _ar_[i] &le; 10<sup>10</sup>**

### Sample Input
```
5
1000000001 1000000002 1000000003 1000000004 1000000005
```

### Output
```
5000000015
```

##### Note:
The range of the 32-bit integer is<br>
**( -2<sup>31</sup> ) _to_ ( 2<sup>31</sup> - 1 ) _or_ [-2147483648, 2147483647]**.<br>
When we add several integer values, the resulting sum might exceed the above range. You might need to use long long int in C/C++ or long data type in Java to store such sums. 