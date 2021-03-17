# Solution

## Task

[115. Distinct Subsequences](https://leetcode-cn.com/problems/distinct-subsequences/)

## Problem

Given two strings ``s`` and ``t``, return the number of distinct subsequences of ``s`` which equals ``t``.

A string's **subsequence** is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., ``"ACE"`` is a subsequence of ``"ABCDE"`` while ``"AEC"`` is not).

It is guaranteed the answer fits on a 32-bit signed integer.

### Example 1
```
Input: s = "rabbbit", t = "rabbit"
Output: 3

Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
[rabb]b[it]
[rab]b[bit]
[ra]b[bbit]
```

### Example 2
```
Input: s = "babgbag", t = "bag"
Output: 5

Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
[ba]b[g]bag
[ba]bgba[g]
[b]abgb[ag]
ba[b]gb[ag]
babg[bag]
```

### Constraints

* 0 <= ``s.length, t.length`` <= 1000
* ``s`` and ``t`` consist of English letters.

## Solution

### Idea
The key point to the problem is **Dynamic Programming**.

That is, ``dp[i][j]`` stores the number of ``t[j:]`` in ``s[i:]``.

The transform formula is:

* if ``s[i]==t[j]``, ``dp[i][j]=dp[i+1][j+1]+dp[i+1][j]``
* if ``s[i]!=t[j]``, ``dp[i][j]=+dp[i+1][j]``
  

## Code
[115. Distinct Subsequences.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-17%20:%20115.%20Distinct%20Subsequences/115.%20Distinct%20Subsequences.cpp)

[115. Distinct Subsequences.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-17%20:%20115.%20Distinct%20Subsequences/115.%20Distinct%20Subsequences.py)

[115. Distinct Subsequences.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-17%20:%20115.%20Distinct%20Subsequences/115.%20Distinct%20Subsequences.java)

