# Solution

## Task

[132. Palindrome Partitioning II](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)


## Problem

Given a string ``s``, partition ``s`` such that every substring of the partition is a palindrome.

Return the *minimum cuts needed* for a palindrome partitioning of ``s``.

### Example 1
```
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

### Example 2
```
Input: s = "a"
Output: 0
```

### Example 3
```
Input: s = "ab"
Output: 1
```

### Constraints

* 1 <= ``s.length`` <= 2000
* ``s`` consists of lower-case English letters only.

## Solution

### Idea
**Dynamic Programming(DP)** for twice.

The first **DP** records whether a substring is a palindrome, while the second **DP** records the minimum cut needed.

## Code
[132. Palindrome Partitioning II](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-07%20:%20132.%20Palindrome%20Partitioning%20II/132.%20Palindrome%20Partitioning%20II.py)
