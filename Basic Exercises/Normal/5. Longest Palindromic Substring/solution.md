# Solution

## Task

[5. Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/)


## Problem

Given a string ``s``, return the **longest palindromic substring** in ``s``.

### Example 1
```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

### Example 2
```
Input: s = "cbbd"
Output: "bb"
```

### Example 3
```
Input: s = "a"
Output: "a"
```

### Example 4
```
Input: s = "ac"
Output: "a"
```

### Constraints

* 1 <= ``s.length`` <= 1000
* ``s`` consist of only digits and English letters (lower-case and/or upper-case).


## Solution

### Idea
**Dynamic Programming(DP)**

Make use of the transition formula ``array[l][r] = (s[l] == s[r]) and array[l+1][r-1]``.

Process in a certain order, otherwise it will cause fatal error.

### Advanced Solution
Please refer to [LeetCode official solution](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/)

## Code
[5. Longest Palindromic Substring](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Normal/5.%20Longest%20Palindromic%20Substring/5.%20Longest%20Palindromic%20Substring.py)
