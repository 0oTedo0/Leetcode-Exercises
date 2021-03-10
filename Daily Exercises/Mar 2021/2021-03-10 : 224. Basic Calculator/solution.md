# Solution

## Task

[224. Basic Calculator](https://leetcode-cn.com/problems/basic-calculator/)


## Problem

Given a string s representing an expression, implement a basic calculator to evaluate it.

### Example 1
```
Input: s = "1 + 1"
Output: 2
```

### Example 2
```
Input: s = " 2-1 + 2 "
Output: 3
```

### Example 3
```
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

### Constraints

* 1 <= ``s.length`` <= 3 * 105
* ``s`` consists of digits, ``'+'``, ``'-'``, ``'('``, ``')'``, and ``' '``.
* ``s`` represents a valid expression.

## Solution

### Idea
Use **Stack** to solve the problem. The **stack** stores the sign of the number.

Remember a number may contain more than one digit.

## Code
[224. Basic Calculator.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-10%20:%20224.%20Basic%20Calculator/224.%20Basic%20Calculator.cpp)

[224. Basic Calculator.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-10%20:%20224.%20Basic%20Calculator/224.%20Basic%20Calculator.py)
