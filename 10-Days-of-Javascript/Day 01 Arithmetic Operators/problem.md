## Objective
In this challenge, we practice using arithmetic operators. Check out the attached tutorial for resources.

## Task
Complete the following functions in the editor below:
1. `getArea(length, width)`: Calculate and return the area of a rectangle having sides `length` and `width`.
2. `getPerimeter(length, width)`: Calculate and return the perimeter of a rectangle having sides `length` and `width`.
The values returned by these functions are printed to stdout by locked stub code in the editor.

## Input Format
`getArea`
| Data Type | Parameter | Description                                  |
|-----------|-----------|----------------------------------------------|
| `Number`  | `length`  | A number denoting the length of a rectangle. |
| `Number`  | `height`  | A number denoting the height of a rectangle. |

`getPerimeter(length, height)`
| Data Type | Parameter | Description                                  |
|-----------|-----------|----------------------------------------------|
| `Number`  | `length`  | A number denoting the length of a rectangle. |
| `Number`  | `height`  | A number denoting the height of a rectangle. |

## Constraints
* 1 &le; `length`,`width` &le; 1000 
* `length` and `width` are scaled to at most three decimal places.

## Output Format
| Function       | Return Type | Description                                                     |
|----------------|-------------|-----------------------------------------------------------------|
| `getArea`      | `Number`    | The area of a rectangle sides `length` and `width`.             |
| `getPerimeter` | `Number`    | The perimeter of a rectangle having sides `length` and `width`. |

## Sample Input 0
```
3
4.5
```

## Sample Output 0
```
13.5
15
```

## Explanation 0
The area of the rectangle is `length` x `width`= 3 x 4.5 = 13.5. <br>
The perimeter of the rectangle is 2 * (`length` + `width`) = 2 * (3 + 4.5) = 15.
