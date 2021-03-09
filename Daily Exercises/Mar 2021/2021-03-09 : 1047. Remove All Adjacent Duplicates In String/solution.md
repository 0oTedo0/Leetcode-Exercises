# Solution

## Task

[1047. Remove All Adjacent Duplicates In String](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/)


## Problem

Given a string ``S`` of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on ``S`` until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

### Example 1
```
Input: "abbaca"
Output: "ca"

Explanation: 
  For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.
  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
```

### Note

* 1 <= ``S.length`` <= 20000
* ``S`` consists only of English lowercase letters.

## Solution

### Idea
Use **Stack** to solve the problem

## Code
[1047. Remove All Adjacent Duplicates In String.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-09%20:%201047.%20Remove%20All%20Adjacent%20Duplicates%20In%20String/1047.%20Remove%20All%20Adjacent%20Duplicates%20In%20String.cpp)
[1047. Remove All Adjacent Duplicates In String.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-09%20:%201047.%20Remove%20All%20Adjacent%20Duplicates%20In%20String/1047.%20Remove%20All%20Adjacent%20Duplicates%20In%20String.py)
