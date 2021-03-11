# Solution

## Task

[224. Basic Calculator](https://leetcode-cn.com/problems/basic-calculator/)


## Problem

Given a string ``s`` which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

### Example 1
```
Input: s = "3+2*2"
Output: 7
```
### Example 2
```
Input: s = " 3/2 "
Output: 1
```
### Example 3
```
Input: s = " 3+5 / 2 "
Output: 5
```

### Constraints

* 1 <= ``s.length`` <= 3 * 105
* ``s`` consists of integers and operators ``('+', '-', '*', '/')`` separated by some number of spaces.
* ``s`` represents a **valid** expression.
* All the integers in the expression are non-negative integers in the range ``[0, 2^31 - 1]``.
* The answer is **guaranteed** to fit in a **32-bit integer**.

## Solution

### Idea
Use **Stack** to solve the problem. The **stack** stores the number after *multiplication* and *division*.

Remember a number may contain more than one digit.

## Code
[227. Basic Calculator II.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-11%20:%20227.%20Basic%20Calculator%20II/227.%20Basic%20Calculator%20II.cpp)

[227. Basic Calculator II.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-11%20:%20227.%20Basic%20Calculator%20II/227.%20Basic%20Calculator%20II.py)
