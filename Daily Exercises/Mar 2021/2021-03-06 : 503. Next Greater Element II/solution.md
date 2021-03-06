# Solution

## Task

[503. Next Greater Element II](https://leetcode-cn.com/problems/next-greater-element-ii/)


## Problem

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

### Example 1
```
Input: [1,2,1]

Output: [2,-1,2]

Explanation: 
  The first 1's next greater number is 2; 
  The number 2 can't find next greater number; 
  The second 1's next greater number needs to search circularly, which is also 2.
```

### Note
The length of given array won't exceed 10000.

## Solution

### Idea
Implement **Monotonic Stack** (decresing).

Mark the elements in stack one by one only when the new element disobey the **monoticity**.

## Code
[503. Next Greater Element II](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-06/503.%20Next%20Greater%20Element%20II.py)
