# Solution

## Task

[92. Reverse Linked List II](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

## Problem

Given the ``head`` of a singly linked list and two integers ``left`` and ``right`` where ``left <= right``,
reverse the nodes of the list from position ``left`` to position ``right``, and return the reversed list.

### Example 1
<img width="350" height="150" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg"/>
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

### Example 2
```
Input: head = [5], left = 1, right = 1
Output: [5]
```

### Constraints

* The number of nodes in the list is ``n``.
* 1 <= ``n`` <= 500
* -500 <= ``Node.val`` <= 500
* 1 <= ``left`` <= ``right`` <= n

## Solution

### Idea
The key point to the problem is double **pointesr of nodes** in list.

You need to figure out how to traverse through the list and meanwhile reversed the list. 

## Code
[92. Reverse Linked List II.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-18%20:%2092.%20Reverse%20Linked%20List%20II/92.%20Reverse%20Linked%20List%20II.cpp)

[92. Reverse Linked List II.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-18%20:%2092.%20Reverse%20Linked%20List%20II/92.%20Reverse%20Linked%20List%20II.py)

[92. Reverse Linked List II.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-18%20:%2092.%20Reverse%20Linked%20List%20II/92.%20Reverse%20Linked%20List%20II.java)

