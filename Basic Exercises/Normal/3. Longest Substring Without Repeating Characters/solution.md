# Solution

## Task

[3. Longest Substring Without Repeating Characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)


## Problem

Given a string ``s``, find the length of the **longest substring** without repeating characters.

### Example 1

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Example 4

```
Input: s = ""
Output: 0
```

### Constraints

* 0 <= ``s.length`` <= 5 * 104
* ``s`` consists of English letters, digits, symbols and spaces.

## Solution

### Idea
Use **Sliding Window** to solve this problem.

**Sliding Window** only traverses of the string for one time, which requires ``O(n)`` run-time overhead.

## Code
**Python 3:** [3. Longest Substring Without Repeating Characters.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Normal/3/3.%20Longest%20Substring%20Without%20Repeating%20Characters.py)

**C++:** [3. Longest Substring Without Repeating Characters.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Normal/3/3.%20Longest%20Substring%20Without%20Repeating%20Characters.cpp)
