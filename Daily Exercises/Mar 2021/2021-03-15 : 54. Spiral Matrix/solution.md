# Solution

## Task

[54. Spiral Matrix](https://leetcode-cn.com/problems/spiral-matrix/)

## Problem

Given an m x n matrix, return all elements of the matrix in spiral order.

### Example 1
<img width="150" height="150" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg"/>

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 2
<img width="200" height="150" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg"/>

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

### Constraints

* ``m`` == ``matrix.length``
* ``n`` == ``matrix[i].length``
* 1 <= ``m, n`` <= 10
* -100 <= ``matrix[i][j]`` <= 100

## Solution

### Idea
The key point to the problem is **Path Simulation**. That is, we need to move step by step to traverse through the matrix in a certain order.

It is necessary to set 4 boundaries (i.e. 4 ''walls'' in the matrix) to record the visited number.

## Code
[54. Spiral Matrix.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-15%20:%2054.%20Spiral%20Matrix/54.%20Spiral%20Matrix.cpp)

[54. Spiral Matrix.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-15%20:%2054.%20Spiral%20Matrix/54.%20Spiral%20Matrix.py)

