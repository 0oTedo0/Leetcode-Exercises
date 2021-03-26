# Solution

## Task

[82. Remove Duplicates from Sorted List II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem

Given the ``head`` of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list **sorted** as well.

### Example 1
<img width="500" height="150" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg"/>

```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

### Example 2
<img width="350" height="150" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg"/>

```
Input: head = [1,1,1,2,3]
Output: [2,3]
```

### Constraints

* The number of nodes in the list is in the range [0, 300].
* -100 <= ``Node.val`` <= 100
* The list is guaranteed to be **sorted** in ascending order.

## Solution

### Idea
**Recursion**

We can simply delete duplicates by recursion.

- If the head is duplicated, remove corresponding nodes, and recurse with new head.
- If the head is not duplicated, recurse with head.next.

## Code
[82. Remove Duplicates from Sorted List II.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-25%20:%2082.%20Remove%20Duplicates%20from%20Sorted%20List%20II/82.%20Remove%20Duplicates%20from%20Sorted%20List%20II.cpp)

[82. Remove Duplicates from Sorted List II.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-25%20:%2082.%20Remove%20Duplicates%20from%20Sorted%20List%20II/82.%20Remove%20Duplicates%20from%20Sorted%20List%20II.py)

[82. Remove Duplicates from Sorted List II.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-25%20:%2082.%20Remove%20Duplicates%20from%20Sorted%20List%20II/82.%20Remove%20Duplicates%20from%20Sorted%20List%20II.java)

