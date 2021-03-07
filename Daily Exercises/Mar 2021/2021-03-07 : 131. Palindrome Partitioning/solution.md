# Solution

## Task

[131. Palindrome Partitioning](https://leetcode-cn.com/problems/palindrome-partitioning/)


## Problem

Given a string ``s``, partition ``s`` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning of ``s``.

A **palindrome** string is a string that reads the same backward as forward.

### Example 1
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```
### Example 2
```
Input: s = "a"
Output: [["a"]]
```

### Constraints

* 1 <= ``s.length`` <= 16
* ``s`` contains only lowercase English letters.

## Solution

### Idea
**Dynamic Programming(DP)** and **Deep First Search(DFS)** with backtracking.

**DP** records whether a substring is a palindrome, while Backtracking **DFS** finds the answer.

## Code
[131. Palindrome Partitioning](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-07%20:%20131.%20Palindrome%20Partitioning/131.%20Palindrome%20Partitioning.py)
