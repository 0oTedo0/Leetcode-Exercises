# Solution

## Task

[341. Flatten Nested List Iterator](https://leetcode-cn.com/problems/flatten-nested-list-iterator/)

## Problem

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

### Example 1
```
Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: 
  By calling next repeatedly until hasNext returns false, 
  the order of elements returned by next should be: [1,1,2,1,1].
```
### Example 2
```
Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: 
  By calling next repeatedly until hasNext returns false, 
  the order of elements returned by next should be: [1,4,6].  
```
## Solution

### Idea
**Depth first search**(not implemented here) or **Stack**

There are two things that you should notice:
  1. the interface class **NestedInteger** is quite useful in your inplementation.
  2. every time before 'next' is called, 'hasNext' is called first

Steps:
  1. initialization: a stack for output
  2. next: return the top element, and move forward
  3. hasNext: if the current list is traversed, pop it and push back the corresponding 'integer' or 'list'


## Code
[341. Flatten Nested List Iterator.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-23%20:%20341.%20Flatten%20Nested%20List%20Iterator/341.%20Flatten%20Nested%20List%20Iterator.cpp)

[341. Flatten Nested List Iterator.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-23%20:%20341.%20Flatten%20Nested%20List%20Iterator/341.%20Flatten%20Nested%20List%20Iterator.py)

[341. Flatten Nested List Iterator.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-23%20:%20341.%20Flatten%20Nested%20List%20Iterator/341.%20Flatten%20Nested%20List%20Iterator.java)
