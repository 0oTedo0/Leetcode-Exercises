# Solution

## Task

[59. Spiral Matrix II](https://leetcode-cn.com/problems/spiral-matrix-ii/)

## Problem

Given a positive integer ``n``, generate an ``n x n`` matrix filled with elements from 1 to n<sup>2</sup> in spiral order.

### Example 1
<img width="150" height="150" src="https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg"/>

```
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
```

### Example 2
```
Input: n = 1
Output: [[1]]
```

### Constraints

* 1 <= ``n`` <= 20

## Solution

### Idea
The key point to the problem is **Path Simulation**. That is, we need to move step by step to traverse through the matrix in a certain order.

It is necessary to set 4 boundaries (i.e. 4 ''walls'' in the matrix) to record the visited number.

## Code
[59. Spiral Matrix II.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-16%20:%2059.%20Spiral%20Matrix%20II/59.%20Spiral%20Matrix%20II.cpp)

[59. Spiral Matrix II.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-16%20:%2059.%20Spiral%20Matrix%20II/59.%20Spiral%20Matrix%20II.py)

