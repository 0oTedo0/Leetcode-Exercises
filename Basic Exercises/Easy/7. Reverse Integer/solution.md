# Solution

## Task

[7. Reverse Integer](https://leetcode-cn.com/problems/reverse-integer/)

## Problem

Given a signed 32-bit integer ``x``, return ``x`` with its digits reversed. If reversing ``x`` causes the value to go outside the signed 32-bit integer range
[-2<sup>31</sup>, 22<sup>31</sup> - 1], then return 0.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

### Example 1
```
Input: x = 123
Output: 321
```

### Example 2
```
Input: x = -123
Output: -321
```

### Example 3
```
Input: x = 120
Output: 21
```

### Example 4
```
Input: x = 0
Output: 0
```

### Constraints

-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

## Solution

### Idea
Reverse the number while noting whether it is out of the range of **int**.

## Code
[7. Reverse Integer.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Easy/7.%20Reverse%20Integer/7.%20Reverse%20Integer.cpp)

[7. Reverse Integer.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Easy/7.%20Reverse%20Integer/7.%20Reverse%20Integer.py)

[7. Reverse Integer.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Easy/7.%20Reverse%20Integer/7.%20Reverse%20Integer.java)
