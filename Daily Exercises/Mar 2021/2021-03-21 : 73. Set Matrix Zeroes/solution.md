# Solution

## Task

[73. Set Matrix Zeroes](https://leetcode-cn.com/problems/set-matrix-zeroes/)

## Problem

Given an ``m x n`` matrix. If an element is **0**, set its entire row and column to **0**. Do it **in-place**.

### Follow up

* A straight forward solution using O(mn) space is probably a bad idea.
* A simple improvement uses O(m + n) space, but still not the best solution.
* Could you devise a constant space solution?
 
### Example 1
<img width="400" height="150" src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg"/>

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

### Example 2
<img width="500" height="150" src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg"/>

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

### Constraints

* ``m`` == ``matrix.length``
* ``n`` == ``matrix[0].length``
* 1 <=`` m, n`` <= 200
* -2<sup>31</sup> <= ``matrix[i][j]`` <= 2<sup>31</sup> - 1

## Solution

### Idea
The key point to the problem is to use **in-place** method to update matrix.

Steps:
  1. find whether there is a **0** in the first column, denoted as ``flag_col``
  2. for every element ``x`` in every column (except for the first column), if ``x`` is **0**, set the corresponding first element in the row and column to **0**
  3. for every element ``x`` in every column (except for the first column), if the corresponding first element in the row and column is **0**, set ``x`` to **0**
  4. if ``flag_col`` is ``true``, set the first column to **0**

## Code
[73. Set Matrix Zeroes.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-21%20:%2073.%20Set%20Matrix%20Zeroes/73.%20Set%20Matrix%20Zeroes.cpp)

[73. Set Matrix Zeroes.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-21%20:%2073.%20Set%20Matrix%20Zeroes/73.%20Set%20Matrix%20Zeroes.py)

[73. Set Matrix Zeroes.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-21%20:%2073.%20Set%20Matrix%20Zeroes/73.%20Set%20Matrix%20Zeroes.java)
