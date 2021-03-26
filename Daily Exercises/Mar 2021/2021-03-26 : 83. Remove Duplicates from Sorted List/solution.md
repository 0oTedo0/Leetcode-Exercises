# Solution

## Task

[83. Remove Duplicates from Sorted List](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)

## Problem

Given the ``head`` of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list **sorted** as well.

### Example 1
<img width="150" height="150" src="https://assets.leetcode.com/uploads/2021/01/04/list1.jpg"/>

```
Input: head = [1,1,2]
Output: [1,2]
```

### Example 2
<img width="150" height="150" src="https://assets.leetcode.com/uploads/2021/01/04/list2.jpg"/>

```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

### Constraints

* The number of nodes in the list is in the range [0, 300].
* -100 <= ``Node.val`` <= 100
* The list is guaranteed to be **sorted** in ascending order.

## Solution

### Idea
**Recursion**

We can simply delete duplicates by recursion.

- If the head is duplicated, remove corresponding nodes, and recurse with new head, after which concatenate head and the processed new head by setting head.next=processed new head.
- If the head is not duplicated, recurse with head.next.

## Code
[82. Remove Duplicates from Sorted List.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-26%20:%2083.%20Remove%20Duplicates%20from%20Sorted%20List/83.%20Remove%20Duplicates%20from%20Sorted%20List.cpp)

[82. Remove Duplicates from Sorted List.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-26%20:%2083.%20Remove%20Duplicates%20from%20Sorted%20List/83.%20Remove%20Duplicates%20from%20Sorted%20List.py)

[82. Remove Duplicates from Sorted List.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-26%20:%2083.%20Remove%20Duplicates%20from%20Sorted%20List/83.%20Remove%20Duplicates%20from%20Sorted%20List.java)

