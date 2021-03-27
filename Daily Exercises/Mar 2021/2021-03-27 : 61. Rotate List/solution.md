# Solution

## Task

[61. Rotate List](https://leetcode-cn.com/problems/rotate-list/)

## Problem

Given the head of a linked list, rotate the list to the right by k places.

### Example 1

<img width="600" height="250" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg"/>

```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```
### Example 2

<img width="450" height="500" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg"/>

```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

### Constraints

* The number of nodes in the list is in the range [0, 500].
* -100 <= ``Node.val`` <= 100
* 0 <= ``k`` <= 2 * 109

## Solution

### Idea
**Double Pointers(fast & slow)** or circular linked list(not inplemented)

Goal: let slow pointer lags behind fast pointer ``k`` step

Note: check which is larger: ``k`` or the length of linked list

Steps:

  1.Traverse the linked list, move fast pointer ``k`` step forward. If it reaches the tail, break the loop immediately (record the length ``i``).

  2.If it breaks the loop, redo step 1 with (``k%i``).

  3.If fast pointer points to head of list, return immediately

  4.Now move fast and slow pointers together until fast pointer reaches the end.

  5.Now, cut the connection between slow and slow.next, and concatenate tail and head by tail.next=head.

  6.Return slow.next

## Code
[61. Rotate List.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-27%20:%2061.%20Rotate%20List/61.%20Rotate%20List.cpp)

[61. Rotate List.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-27%20:%2061.%20Rotate%20List/61.%20Rotate%20List.py)

[61. Rotate List.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-27%20:%2061.%20Rotate%20List/61.%20Rotate%20List.java)

