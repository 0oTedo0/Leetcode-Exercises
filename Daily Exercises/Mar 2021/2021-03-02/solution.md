# Solution

## Task

[304. Range Sum Query 2D - Immutable](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/)


## Problem:

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner ``(row1, col1)`` and lower right corner ``(row2, col2)``.

<img width="150" height="150" src="https://assets.leetcode-cn.com/aliyun-lc-upload/images/304.png"/>

The above rectangle (with the red border) is defined by (row1, col1) = **(2, 1)** and (row2, col2) = **(4, 3)**, which contains sum = 8.

### Example 1

```
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
```

### Note

* You may assume that the matrix does not change.
* There are many calls to sumRegion function.
* You may assume that row1 ≤ row2 and col1 ≤ col2.

## Solution

### Idea
Use **Dynamic programing(DP)** to solve the problem.

**DP** requires ``O(mn)`` time for initialization and ``O(mn)`` space for storing the created array ``self.sums``, but query time becomes ``O(1)``.

## Code
[304. Range Sum Query 2D - Immutable](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-02/304.%20Range%20Sum%20Query%202D%20-%20Immutable.py)
