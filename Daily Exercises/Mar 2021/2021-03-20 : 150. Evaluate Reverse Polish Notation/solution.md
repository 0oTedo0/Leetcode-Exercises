# Solution

## Task

[150. Evaluate Reverse Polish Notation](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)

## Problem

Evaluate the value of an arithmetic expression in [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Valid operators are ``+``, ``-``, ``*``, and ``/``. Each operand may be an integer or another expression.

**Note** that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

### Example 1
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

### Example 2
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

### Example 3
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

### Constraints

* 1 <= ``tokens.length`` <= 104
* ``tokens[i]`` is either an operator: ``"+"``, ``"-"``, ``"*"``, or ``"/"``, or an integer in the range [-200, 200].

## Solution

### Idea
The key point to the problem is **Stack**.

In each iteration, we push a number, or pop 2 numbers when encoutering an operation and then push the result back.

## Code
[150. Evaluate Reverse Polish Notation.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-20%20:%20150.%20Evaluate%20Reverse%20Polish%20Notation/150.%20Evaluate%20Reverse%20Polish%20Notation.cpp)

[150. Evaluate Reverse Polish Notation.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-20%20:%20150.%20Evaluate%20Reverse%20Polish%20Notation/150.%20Evaluate%20Reverse%20Polish%20Notation.py)

[150. Evaluate Reverse Polish Notation.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-20%20:%20150.%20Evaluate%20Reverse%20Polish%20Notation/150.%20Evaluate%20Reverse%20Polish%20Notation.java)
